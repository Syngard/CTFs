# [Crypto] Zipzipzip 

## Déchiffrement du fichier
On se retrouve avec un fichier `flag.zip.enc` qui sera donc un zip chiffré. Une manière typique de chiffrer des fichiers dans ce type d'épreuves est un simple XOR. Grâce aux propriétés du XOR, on peut retrouver la clé (ou au moins une partie) en connaissant le fichier clair original. Ici on sait que le fichier est une archive ZIP. On regarde donc quels sont les premiers octets caractéristiques (aussi appelés *magic bytes*) de ce type de fichiers. Wikipedia nous donne la réponse (https://en.wikipedia.org/wiki/List\_of\_file\_signatures) : `50 4B 03 04`. En XORant ces octets avec les quatre premiers du fichier chiffré on peut ainsi récupérer la clé de chiffrement.

```python
with open('flag.zip.enc', 'rb') as f:
  enc = f.read()

MAGIC = b'PK\x03\x04'

key = [i^j for i,j in zip(MAGIC, enc)]
print(key)
```

Le programme nous donne : `\x13\x37\x13\x37`. On voit déjà une répétition et donc on est à peu près certain d'avoir la clé : `\x13\x37` (leet en leet-speak).
Il faut ensuite utiliser cette clé pour déchiffrer l'intégralité du fichier.

```python
from itertools import cycle

with open('flag.zip.enc', 'rb') as f:
  enc = f.read()

KEY = b'\x13\x37'

with open('flag.zip','wb') as g:
  dec = [i^j for i,j in zip(cycle(KEY), enc)]
  for i in dec:
    g.write(bytes([i]))
```


## Récupération du flag
On pourrait penser en avoir fini avec ce challenge mais il recèle une petite surprise. En effet, l'archive est chiffrée avec un mot de passe que l'on ne connait pas. Heureusement un élement va venir jouer en notre faveur.

```bash
$ unzip flag.zip
Archive:  flag.zip
[flag.zip] darkc0de.txt password: 
password incorrect--reenter: 
   skipping: darkc0de.txt            incorrect password
   skipping: flag.txt                incorrect password
```


### Première méthode : Attaque par clair connu
L'archive, en plus du fichier `flag.txt`, contient un fichier nommé `darkc0de.txt`. Une recherche google sur ce nom nous permet de voir qu'il s'agit d'une *wordlist* contenant des mots de passe, à la manière de `rockyou.txt`. On le télécharge depuis l'un des répertoires github où il est présent afin de pouvoir s'en servir dans une attaque de "texte clair connu" (*known plaintext*) contre le chiffrement zip. On utilisera l'outil `pkcrack` pour ça.

```
$ wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/darkc0de.txt
[...]
$ zip darkc0de.zip darkc0de.txt 
  adding: darkc0de.txt (deflated 68%)
$ pkcrack -C flag.zip -c darkc0de.txt -P darkc0de.zip -p darkc0de.txt -d decrypted.zip -a
[...]
Lowest number: 112 values at offset 4815981
Lowest number: 84 values at offset 4815980
Done. Left with 84 possible Values. bestOffset is 4815980.
Stage 1 completed. Starting stage 2 on Thu Feb 13 15:08:34 2020
Ta-daaaaa! key0=d9b118b6, key1= f20085a, key2=efd77a64
Probabilistic test succeeded for 41389 bytes.
Stage 2 completed. Starting zipdecrypt on Thu Feb 13 15:08:35 2020
Decrypting darkc0de.txt (faf3d04cd450305fe58c9704)... OK!
Decrypting flag.txt (4f4fac78be187bc848868c04)... OK!
Finished on Thu Feb 13 15:08:35 2020
```

Il ne reste plus qu'à déchiffrer le zip et à lire le flag.

```
$ unzip decrypted.zip 
Archive:  decrypted.zip
replace darkc0de.txt? [y]es, [n]o, [A]ll, [N]one, [r]ename: n
 extracting: flag.txt 
$ cat flag.txt
HSR{Kp74_x0r_1s_n07_s3cUrEd} 
```

### Deuxième méthode : Attaque par dictionnaire
Etant donné que le fichier `darkc0de.txt` est un dictionnaire de mots de passe, on pouvait aussi penser à utiliser cette liste pour ouvrir le zip, et c'était également une méthode valable. On extrait dans un premier temps le hash du mot de passe du zip, puis on tente de le cracker avec le dictionnaire que l'on vient de récupérer.

```
$ zip2john flag.zip  > hash.john 
[...]
$ john --wordlist=$(pwd)/darkc0de.txt hash.john
[...]
$ john --show hash.john                                                                
flag.zip:mic12013pid0p7312::flag.zip:flag.txt, darkc0de.txt:flag.zip
```

On peut ensuite déchiffrer l'archive en utilisant le mot de passe `mic12013pid0p7312` pour récupérer le flag.

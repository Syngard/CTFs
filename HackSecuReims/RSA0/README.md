#[Crypto] RSA0 

En dézippant l'archive fournie, on se retrouve avec un fichier `enc.txt` qui contient une liste de nombres, ainsi que le script `rsa0.py` ayant servi à chiffrer le flag. En lisant ce script, on voir que chaque caractère du message clair est chiffré indépendamment des autres. On peut donc appliquer la même méthode que pour le challenge `hashes` : 
  * Construire un dictionnaire associant les caractères à leur valeur chiffrée (que l'on peut simplement recalculer puisque l'on dispose de la clé publique).
  * Parcourir la liste de nombres du fichier `enc.txt` pour reconstruire le flag

J'ai simplement réutilisé mon script du challenge `hashes` en remplaçant le calcul du hash par un calcul du chiffré pour chaque caractère.

```python
import string

# Public Parameters
e = 65537
N = 25026500722700304586546032040035835214278430580279591319431625768374734987653757098701139593537352808125833859561574001990371167171016948717751877968164912345887291658689837128210679316535060365347405138414557982360642551204566056439699797828776200852154364925143904871851293017621601440640917426330846547220254206630287542080735851469428744379549917271244027256143062163613041570302762383492661189936552676775913519674013715398169240910047303078530486721711689038462511290815905976933585763848151541719130592687879243459735469502485549478058192149823974570730857379101264143073526751378505066500635790988130715279299

flag = ""
d = {}
for i in string.printable:
  c = pow(ord(i), e, N)
  d[c] = i

with open('enc.txt') as enc:
  while(1):
    c = int(enc.readline()[:-1])  
    flag += d[c]

  print(flag)
```

En exécutant le programme, on trouve : 

```

 _   _ ____  ____   ______  _____       _ _           ____  ____    _    
| | | / ___||  _ \ / /  _ \|___ /  __ _| | |_   _    |  _ \/ ___|  / \   
| |_| \___ \| |_) | || |_) | |_ \ / _` | | | | | |   | |_) \___ \ / _ \  
|  _  |___) |  _ < < |  _ < ___) | (_| | | | |_| |   |  _ < ___) / ___ \ 
|_| |_|____/|_| \_\ ||_| \_\____/ \__,_|_|_|\__, |___|_| \_\____/_/   \_               
                   \_\                      |___/_____|                  
      _       ____  _                                _     _ _____ 
     | |__   / __ \| |__  _   _      _ __  _ __ ___ | |__ | |___ / 
     | '_ \ / / _` | '_ \| | | |    | '_ \| '__/ _ \| '_ \| | |_ \ 
     | |_) | | (_| | |_) | |_| |    | |_) | | | (_) | |_) | |___) |
 ____|_.__/ \ \__,_|_.__/ \__, |____| .__/|_|  \___/|_.__/|_|____/ 
|_____|      \____/       |___/_____|_|                            
               _____ _____    __   
 _ __ ___     | ____|__  /    \ \  
| '_ ` _ \    |  _|   / /      | | 
| | | | | |   | |___ / /_ _ _ _ > >
|_| |_| |_|___|_____/____(_|_|_) | 
         |_____|              /_/  
 
```

Le flag est en ASCII-art et il faut simplement le retranscrire : HSR{R3ally\_b@by\_probl3m\_EZ...}


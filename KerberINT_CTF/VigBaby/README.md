# Vig Baby challenge writeup

**Category:** Crypto

**Description:**

> Encrypted flag : TKlc\_OLxUOhJMGbiVa0mhjHifvG6JiHDJZnhJ7ULikhxLra

> Encryption program :
```python
#!/usr/bin/python

import hashlib
import sys
from itertools import cycle

ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_{}'

def encrypt(key, plaintext):
    """Encrypt the string and return the ciphertext"""
    pairs = zip(plaintext, cycle(key))
    result = ''

    for pair in pairs:
        (x,y)=pair
        #print(x,y)
        total = ALPHA.index(x) + ALPHA.index(y)
        result += ALPHA[total % len(ALPHA)]

    return result

key=sys.argv[1]
plaintext=sys.argv[2]+key
cipher=encrypt(key,plaintext)
print(cipher)
```

## Solution write-up

From the name of the challenge, we can guess that this will be some kind of Vigenere cipher. But first let's understand what the `zip(plaintext, cycle(key))` does.

```
$ python    
>>> from itertools import cycle   
>>> zip("plaintext",cycle("123"))   
[('p', '1'), ('l', '2'), ('a', '3'), ('i', '1'), ('n', '2'), ('t', '3'), ('e', '1'), ('x', '2'), ('t', '3')]
```

Along with a bit of [documentation](https://docs.python.org/2/library/itertools.html#itertools.cycle), we can understand that `zip` pairs characters in the same position and cycle allows to repeat the key when all if its letters are used. So the `encrypt` function is a Vigenere cipher, but that operates on a larger alphabet compared to the [original version](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher). 


It's a standard cipher and we already know the first four characters of the plaintext, so we can easily retrieve the first four letters of the key. Let's write a function that does the exact opposite of the `encrypt` that we are given, and let's call it `decrypt`. The only thing we have to do here is change the '+' sign to a '-' sign . It will simply decrypt the ciphertext with the given key. 

```python
def decrypt(key, ciphertext):
    pairs = zip(ciphertext, cycle(key))
    result = ''
    
    for pair in pairs:
        (x,y)=pair
        total = ALPHA.index(x) - ALPHA.index(y)
        result += ALPHA[total % len(ALPHA)]

    return result
```

Then we need a function to try all possible letters and check which one gives us the known plaintext (in this case, "CTF{").

```python
def find_key(cipher,clear):
    key = ''
    for i in range(len(clear)):
        for j in ALPHA:
            key_tmp = key + j
            test_decrypt = decrypt(key_tmp, cipher)
            if (test_decrypt[i] == clear[i]):
                key += j
                break
    return key
```

Let's test that with what we know.

```python
print find_key(ciphertext, "CTF{")
```
```
$ ./vig\_baby.py   
R4ge
```

A leet speak word. Seems reasonable to think we're on the right track as keys/flags are often leet speak sentences.
But now comes the hard part. Since we don't know the following letters, we can't apply the same method. However, we noticed earlier that the encrypted text wasn't only the flag.

```python
plaintext=sys.argv[2]+key
cipher=encrypt(key,plaintext)
```

The key is actually encrypted with itself alongside the flag. The main problem here is that we don't know the lengh of the flag nor that of the key. This means that we'll have to try every possible key length, at least at the begining. Since `text = flag + key`, it is guaranteed that `len(key) < len(text)` and thus we know for sure that at least the first letters of the key are reused in the encryption process. Since we don't have anymore clues, I decided to check every possible key lengh by decrypting the 5 letters blocks starting from each letter after the beginning of the flag that we know for sure. The fifth letter (actually the first one of the known text here) is a `}`, since we know that it is the last character of the actual flag. 

```python
# Returns the key used to encrypt clear into cipher
def find_key(cipher,clear):
    key = ''
    for i in range(len(cipher)):
        for j in ALPHA:
            key_tmp = key + j
            test_decrypt = decrypt(key_tmp, cipher)
            if (test_decrypt[i] == clear[i]):
                key += j
                break
    return key

def display_possibilities(cleartext, ciphertext):
    k = len(key)
    for i in range(k, len(ciphertext)-k):
        cipher = ciphertext[i:i+k]
        key_test = find_key(cipher, key)
        print "i="+str(i)+" >> "+key_test


key = "}R4ge"
display_possibilities(key, ciphertext)
```

This will give us every possible key used to decrypt the known block at all possible positions in the text.

```
$ ./vigEasy.py 
i=5 >> P761x
i=6 >> MgdvD
i=7 >> yDXBs
i=8 >> V_qqv
i=9 >> PQStp
i=10 >> i5Vn_
i=11 >> K8P8E
i=12 >> N2kC4
i=13 >> HKr29
i=14 >> cRe7W
i=15 >> jEjUI
i=16 >> WJ9GD
i=17 >> bjvBF
i=18 >> 1VqDq
i=19 >> nQsoE
i=20 >> iSQCB
i=21 >> k3r}R
i=22 >> IRoPp
i=23 >> jO4nc
i=24 >> gePas
i=25 >> w2CqE
i=26 >> HpSCq
i=27 >> 75rom
i=28 >> KRQks
i=29 >> j3Mq8
i=30 >> IzS6J
i=31 >> E5iHD
i=32 >> KIwBs
i=33 >> aWqqd
i=34 >> oQSb3
i=35 >> i5D1u
i=36 >> KqdsE
i=37 >> 8DUCG
i=38 >> V7rED
i=39 >> MRtBT
i=40 >> jTqRu
i=41 >> lQ6sN
```

Now we have to look in there for something that, at best, is the beginning of the key itself ; or that seems like leet speak (that would make it highly probable that it is a part of the key). Luckily, there is a result that matches what we're looking for.

```
i=24 >> gePas
```

The first two letters are the last two ones from the already-known part of the key, and the rest is an actual word that makes sense with the first one (TN : "Rage pas" means "Don't rage" in French). 

With that we can then find the length of the flag. Since the encrypted text is 47 characters long, and since the 24th to 28th characters of the cleartext are "}R4ge", the encryped key starts from the 25th character.  
So `len(flag) = 25` and `len(key) = 22`

We also found the following letters of the key. Now all we have to do is use the part of the key we know as a cleartext to find the next letters.


```python
def retrieve_key(base_key, ciphertext):
    key = base_key
    while (len(key) != 23):
        k = len(key)
        cipher = ciphertext[24:24+k]
        key = "}R4" + find_key(cipher, key)
        print key

key = "}R4gePas"
retrieve_key(key, ciphertext)
```

```
$ ./vigEasy.py 
}R4gePasTuY
}R4gePasTuY3sP
}R4gePasTuY3sPres
}R4gePasTuY3sPresqu3
}R4gePasTuY3sPresqu3707
```

And there is our key ! Now all we have to do is to decrypt the entire flag with it

```python
key = "R4gePasTuY3sPresqu3707"
print decrypt(key, ciphertext)
```

```
$ ./vigEasy.py 
CTF{v1gen3re_c_3st_sup3r}R4gePasTuY3sPresqu3707
```

And we finally get the flag `CTF{v1gen3re_c_3st_sup3r}`


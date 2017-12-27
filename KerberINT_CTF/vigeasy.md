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

$ python    
\>\>\> from itertools import cycle   
\>\>\> zip("plaintext",cycle("123"))   
[('p', '1'), ('l', '2'), ('a', '3'), ('i', '1'), ('n', '2'), ('t', '3'), ('e', '1'), ('x', '2'), ('t', '3')]


Along with a bit of [documentation](https://docs.python.org/2/library/itertools.html#itertools.cycle), we can understand that `zip` pairs characters in the same position and cycle allows to repeat the key when all if its letters are used. So the `encrypt` function is a Vigenere cipher, but that operates on a larger alphabet compared to the [original version](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher). 


It's a standart cipher and we already know the first four characters of the plaintext, so we can easily retrieve the first four letters of the key. Let's write a function that does the exact opposite of the `encrypt` that we are given, and let's call it `decrypt`. The only thing we have to do here is change the '+' sign to a '-' sign . It will simply decrypt the ciphertext with the given key. 

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

$ ./vig\_baby.py   
R4ge


A leet speak word. Seems reasonable to think we're on the right track as keys/flags are often leet speak sentences.

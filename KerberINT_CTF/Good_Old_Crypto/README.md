# Good Old Crypto challenge writeup

**Category:** Crypto (duh !)

**Description:**

> Encrypted flag : xxhsmbgpogovffoqcrgkqneemgedoneeaeeihzgjkutjlvcpgnpjhjldlppqwgimdofcnrttz

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
        result += ALPHA[total % 26]

    return result.lower()

key=sys.argv[1]
plaintext=sys.argv[2]+key
cipher=encrypt(key,plaintext)
print(cipher)
```

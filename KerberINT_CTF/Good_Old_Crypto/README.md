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

## Solution write-up

Since this challenge is really similat to [VigBaby](../VigBaby), I won't detail the whole solution but will rather focus on the differences.  
The only actual difference in the encryption between this challenge and VigBaby is that we now have some kind of loss of information. The reason for that is that the encrypted char is given `mod 26`, 

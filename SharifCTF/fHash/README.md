# fHash challenge writeup

**Category:** Crypto - 200 points

**Description:**

>  We designed a hash function called "fHash". fHash takes a message (M), as well as two initialization values, designated as left (hl) and right (hr). You can find the implementation of fHash [here](./fHash.py).

> Let M1 = '7368617269666374'. Notice that fHash('7575', 'A8A8', M1) = '260c01da'.
> Find M2 ≠ M1, as well as two initialization values hl and h2, such that fHash(hl, hr, M2) = '260c01da'. That is, find a second-preimage for M1.
> Each of hl and hr must be two bytes, while M2 must be 8 bytes. 


## Solution write-up

By looking at the given implementation of fHash, we see that :
* It takes 3 inputs : one that is 8 bytes long (called `M`) and two that are 2 bytes long (`hl` and `hr`).
* It cuts M into four two-bytes values
* For each of the smaller inputs (`hl` and `hr`):
    * It concatenates it with the first section M
    * It hashes the resulting string with md5
    * It replaces the value of hl/hr with the first two bytes of the hash
    * It repeats the operation with this new value and the second section of `M`, then with the third and the last one
* It returns the concatenation of the final values of `hl` and `hr`

We have to find another value `M2`, as well as the corresponding `hl` and `hr`, that will hash to the same result as the given example.
To be clearer, I'll name the `hl` and `hr` variables with a number corresponding to the number of rounds. So the output will be `hl4 + hr4`. From that we have to determine `hl0` and `hr0`, as well as `M2`.


Since `hl3` and `hr3` are hashes themselves, I will only work with an alphabet comprised of 0-9 and A-F. We have to find a 2-byte word (that will be the last part of `M2`) and 2 others (`hl3` and `hr3`) that, when concatenated with the first one and hashed give `hr4` and `hl4`.

```python
from hashlib import md5
import itertools

ALPHA = "0123456789abcde"

def foo(h, m):
    return md5(h.encode('utf-8') + m.encode('utf-8')).hexdigest()[:4]


def round(hl, m, hr):
    return foo(hl, m), foo(hr, m)


def fHash(hl, hr, M):
    message = list(map(''.join, zip(*[iter(M)] * 4)))
    for m in message:
        hl, hr = round(hl, m, hr)
    return hl + hr


if __name__ == '__main__':
    #print(fHash('7575', 'A8A8', '7368617269666374'))
    #old = ['7368','6172','6966','6374']
    
    hl4 = '260c'
    hr4 = '01da'

    stop = False
    words = list(''.join(i) for i in itertools.product(ALPHA, repeat=4))

    for m2 in words:
        m = ''.join(m2)
        hr_col = False
        hl_col = False

        for h2 in words:
            h = ''.join(h2)

            hash_word = foo(h, m)

            #print "h = "+ h +" // m = "+ m +" // hash = "+ hash_word

            if (hash_word == hl4):
                print "hl collision found"
                print "hl0 = "+ h +" // m3 = "+ m
                hl_col = True

            if (hash_word == hr4):
                print "hr collision found"
                print "hr0 = "+ h +" // m3 = "+ m
                hr_col = True

            if (hl_col and hr_col):
                print 'Found !'
                stop = True
                break

        if (stop):
            break

```

This gives us the last part of `M2` as well as `hr3` and `hl3`. We can also see that there are a lot of different solutions that give the correct hashes. Once this part is done, we only have to save the values we found and do exactly the sae thing but to find the third part of `M2`, `hl2` and `hr2`. And 2 more times after that.

Once we have the 4 parts of `M2`, `hl0` and `hr0` we fill in the form on the website and it gives us the flag.

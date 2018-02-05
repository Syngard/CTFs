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
* For each of the smaller inputs (`hl and `hr`):
    * It concatenates it with the first section M
    * It hashes the resulting string with md5
    * It replaces the value of hl/hr with the first two bytes of the hash
    * It repeats the operation with this new value and the second section of M, then with the third and the last one
* It returns the concatenation of the final values of `hl` and `hr`

We have to find another value M2, as well as the corresponding hl and hr, that will hash to the same result as the given example.


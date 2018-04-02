# Intro to RSA challenge writeup

**Category:** Crypto - 50

**Description:**

> One common method of public key encryption is the RSA algorithm. Given [p, q, e, and c](intro_rsa.txt), see if you can recover the message and find the flag!

## Solution write-up

This is pretty straightforward. Since we already have the private key, we recompute n, phi(n) and d.


```python
n = p * q

phi = (p - 1) * (q - 1)

gcd, a, b = egcd(e, phi)
d = a%phi
```

We then use this to decrypt the ciphertext and convert the hex values to characters.

```python
print hex(pow(ct, d, n))[2:-1].decode('hex')
```
And we get the flag.

```
$ python AngstromCTF/rsa.py 
n:
21352266238858778918619188364794978247110814344182718789531556175082704973662511799212145884523052872549643381551198603804033719877686687407781741732322043789156274178275720788354832936150643106222286829304293720596869272863494431378766446272915418128369306095430212473726823901476758141344180252291976631369541623320758888804504264553726119584590976734678686674325922984357442723564969123266321770925673884391941837791313900158153585513086482758319025962683568257260424117239658488673211483816127597516537553300240648535631202355088566602692908460474280433161774838712563820246482153755227324445454831301552975999253
pt: actf{rsa_is_reallllly_fun!!!!!!}
```
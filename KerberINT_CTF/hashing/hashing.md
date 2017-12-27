# Hashing challenge writeup

**Category:** Crypto

**Description:**

> Hashed flag : 612eb3c0d9879006cb2beef6fa3c8cd2

> Hashing script :   
#! /bin/bash  
secret=$(cat /dev/urandom | tr -dc 'a-z' | fold -w 5 | head -n 1)   
flag=CTF\{$secret\}   
echo $flag   
echo -n $flag | md5sum   

## Solution write-up
First thing we should try to do when faced with a script is trying to figure out what it does. Since this one is given to us and uses not so common commands (tr and fold), the best thing to do is simply to run it a few times.

$ ./hashing.sh   
CTF{owukk}   
f8abf8ef98a83ffd7c5145320da34a58    
   
$ ./hashing.sh    
CTF{vuihv}   
66b6f58f9d61e2033042829679d8ea68   

With that, we can figure out that it is generating a random 5-letter string and putting it inside the CTF{ } tags. It then hashes the output with MD5 and prints both strings. We are given a hashed version of the flag, so we simply have to find the 5-letter string that corresponds to it.



The easiest way to enumerate all possibilites is with a small python script. 

```python
#! /usr/bin/python

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for a in alphabets:
    for b in alphabets:
        for c in alphabets:
            for d in alphabets:
                for e in alphabets:
                    flag = "CTF{"+a+b+c+d+e+"}"
```

A quick google search give us a function to [calculate the md5sum of a string](https://stackoverflow.com/questions/16874598/how-do-i-calculate-the-md5-checksum-of-a-file-in-python). 
We use it and compare the output to the hashed flag we were given at the beginning. When the two matches, we just have to give back the non-hashed flag.

```python
#! /usr/bin/python

import hashlib

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

flag_sum = "612eb3c0d9879006cb2beef6fa3c8cd2"

for a in alphabets:
    for b in alphabets:
        for c in alphabets:
            for d in alphabets:
                for e in alphabets:
                    flag = "CTF{"+a+b+c+d+e+"}"
                    m = hashlib.md5(flag).hexdigest()
                    if (str(m) == flag_sum):
                        print flag
```

After a few seconds wait, the script gives us the flag.



$ ./hashing.py  
CTF{tcvlb}


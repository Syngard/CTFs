# nohtyp1 challenge writeup

**Category:** Crypto

**Description:**

> We love snakes.

> [Linked program](./nohtyp1.py)

> Hints:
```
$ cat flag | md5sum
5a76c600c2ca0f179b643a4fcd4bc7ac
```


## Solution write-up

Since the script is obfuscated, we should try at first to reorganize it to understand what is does.

```python
____=input;
__________________=print;
___________=____();
_________=map;
__________=ord;
_______________=zip;
____________________________=list;
___=21;
_____=lambda ______,_______:______+(_______^___);

______________={not not not ___ and not not ___:lambda:__________________('\x41\x6c\x6d\x6f\x73\x74\x21\x21'),not not ___ and not not ___:lambda:__________________('\x43\x6f\x72\x72\x65\x63\x74\x21')};

______________[[_____(*________) for ________ in _______________(____________________________(_________(__________,___________)),____________________________(_________(__________,___________))[::-1])][::-1]==[160,155,208,160,190,215,237,134,210,126,212,222,224,238,128,240,164,213,183,192,162,178,163,162] and 'mo4r' in ___________ and '34C3_' in ___________ and ___________.split('_')[3] == 'tzzzz']()
```

Apparently, it is renaming some functions with non-readable names and then applying them to some values. Next, we have to rename everything so as to understand what is actually happening here.

```python
#____=input; (4)
#__________________=print; (18)
#___________=input(); (11)
#_________=map;  (9)
#__________=ord; (10)
#_______________=zip; (15)
#____________________________=list; (28)
#___=21; (3)
#olol = _____ (5)
#correct = ______________ (14)

data = input();
olol = lambda a,b : a+(b^21);

correct = {False: lambda: print('Almost!!'), True: lambda: print('Correct!')};

correct[[olol(*a) for a in zip(list(map(ord,data)), list(map(ord,data))[::-1])][::-1]==   
[160,155,208,160,190,215,237,134,210,126,212,222,224,238,128,240,164,213,183,192,162,178,163,162]   
and 'mo4r' in data and '34C3_' in data and data.split('_')[3] == 'tzzzz']()
```

The `correct` function will print if the given password was correct or not depending on how the boolean expression given as a parameter will evaluate. We can break the expression down into two different conditions :

```python
olol(*a) for a in zip(list(map(ord,data)), list(map(ord,data))[::-1])][::-1] ==   
[160,155,208,160,190,215,237,134,210,126,212,222,224,238,128,240,164,213,183,192,162,178,163,162]
```
The data encrypted with the `olol` function must be equal to this array. We'll explore later how exactlty is the encryption done.

```python
'mo4r' in data and '34C3_' in data and data.split('_')[3] == 'tzzzz'
```
The clear flag must contain the words "mo4r", "34C3\_" and "tzzzz". However, since we know the format of the flag, we can go a bit further. The flag will actually start with "34C3\_", and is likely to end with "\_tzzzz" (since "tzzzz" is extracted with `data.split('_')`, it must be preceded by an underscore). So our flag is in the format : "34C3\_" + ...mo4r... + "\_tzzzz".


Now let's move on to the encryption part.  
We can see that the `olol` function is applied to an array of tuples (containing 2 elements each), and the resulting array is then compared to the fixed one given in the code. How exactly is the array of tuples constructed ?

```python
olol(*a) for a in zip(list(map(ord,data)), list(map(ord,data))[::-1])][::-1]
```

```
$ pyhton
>>> data = "flag"
>>> map(ord, data)
[102, 108, 97, 103]
```
The [ord](https://docs.python.org/2/library/functions.html#ord) function returns the ASCII value of a char. The [map](http://book.pythontips.com/en/latest/map_filter.html) function applies a function to all the items in an input list. This part returns a list of the ASCCI values of the chars composing the string.

```
>>> map(ord, data)[::-1]
[103, 97, 108, 102]
```
The `[::-1]` reverses the order of the elements in the list.

```
>>> zip(a, a[::-1])
[(102, 103), (108, 97), (97, 108), (103, 102)]
```
Finally, [zip](https://docs.python.org/2/library/functions.html#zip) pairs elements one to one from its first and second arguments.  
  
It is also important not to forget that the resulting list will be reversed as well before beeing compared.

With that knowledge, we know understand that the first character of the flag will be encrypted with the last one, the second with the second last, etc... We have to recover the flag two characters at the time, starting from both ends. In a first time, we can verify our assumptions on the flag format.

```python
olol = lambda a,b : a+(b^21)

flag_b = "34C3_"  # Since we will have to construct it from the middle
flag_e = "_tzzzz" # let's separate the flag into a beginning and an end part

ciphered_flag = [160,155,208,160,190,215,237,134,210,126,212,222,224,238,128,240,164,213,183,192,162,178,163,162]

test_flag = flag_b + flag_e
test_flag_ciphered = [olol(*a) for a in zip(list(map(ord,test_flag)), list(map(ord,test_flag))[::-1])][::-1] 

print test_flag_ciphered
```

```
$ python nohtp1_solve.py 
[160, 155, 208, 160, 190, 169, 192, 162, 178, 163, 162]
```

We can see that the first 5 values match the values in the `ciphered_flag` array, and the same is true for the last 5 ones. So our assumption about the flag format was correct. However, the 6th value does not correspond to anything in the array we want to obtain. That's because, since our `test_flag` is 11 characters long, the middle one will be encrypted with itself. We shoud then try to find with which character it shoud be encrypted to give the expected values at the positions we want in the resulting array (meaning 215 at the 6th position and 183 at the 6th starting from the end)

```python
import string

# I supposed that the flag probably only included letters, numbers and underscores
# but no other special character
ALPHA = string.ascii_letters + string.digits + '_'
olol = lambda a,b : a+(b^21)

flag_b = "34C3_"
flag_e = "_tzzzz"

ciphered_flag = [160,155,208,160,190,215,237,134,210,126,212,222,224,238,128,240,164,213,183,192,162,178,163,162]

k = len(flag_b)
for i in ALPHA:
    test_flag = flag_b + i + flag_e
    test_flag_ciphered = [olol(*a) for a in zip(list(map(ord,test_flag)), list(map(ord,test_flag))[::-1])][::-1]

    if (test_flag_ciphered[k] == ciphered_flag[k] and test_flag_ciphered[-k-1] == ciphered_flag[-k-1]):
        print test_flag
```

```
$ python nohtp1_solve.py 
34C3_m_tzzzz
```

Okay so the first letter after "34C3\_" is an 'm'. Now we can try to find the characters 2 by two. One that goes after the 'm' and the other that will land just before the "\_tzzzz".

```python
flag_b = "34C3_m" # Since we found that an 'm' should follow I added it direcly 
flag_e = "_tzzzz"

for i in ALPHA:
    for j in ALPHA:
        test_flag = flag_b + i + j +flag_e
        test_flag_ciphered = [olol(*a) for a in zip(list(map(ord,test_flag)), list(map(ord,test_flag))[::-1])][::-1]

        k = len(flag_b)

        if (test_flag_ciphered[k] == ciphered_flag[k] and test_flag_ciphered[-(k+1)] == ciphered_flag[-(k+1)]):
            print test_flag
```

```
$ python nohtp1_solve.py 
34C3_mfz_tzzzz
34C3_mnr_tzzzz
34C3_mos_tzzzz
```

Ah, this time there are several possibilities. However, since we know that the flag must contain the word "mo4r", the last one is the most likely to be the one we are looking for. We could then just add manually the letters to our `flag_b` and `flag_e` variables, but that wouldn't be any fun. So let's automate that a bit. Since there are several possibilities each time, we're also going to use the hint that gives us the md5sum of the flag to stop when we have the right one.

```python
possible_flags = [[flag_b, flag_e]] # All potential flags
mo4r_test_flags = [] # Potential flags that contain "mo4r"

checked = False
while (not checked):
    new_possible_flags = []
    for [flag_b, flag_e] in possible_flags:
        for i in ALPHA:
            for j in ALPHA:
                test_flag = flag_b + i + j +flag_e
                test_flag_ciphered = [olol(*a) for a in zip(list(map(ord,test_flag)), list(map(ord,test_flag))[::-1])][::-1]
                #print test_flag_ciphered
            
                k = len(flag_b)
            
                if (test_flag_ciphered[k] == ciphered_flag[k] and test_flag_ciphered[-(k+1)] == ciphered_flag[-(k+1)]):
                    if ("mo4r" in test_flag and test_flag.count('_') == 3 and len(test_flag) == len(ciphered_flag)):
                        print test_flag
                        mo4r_test_flags.append(test_flag)
                    new_possible_flags.append([flag_b+i,j+flag_e])
    
    possible_flags = new_possible_flags
```

```
$ python nohtp1_solve.py 
34C3_mo4r_sajn4kes_tzzzz
34C3_mo4r_schn4kes_tzzzz
34C3_mo4r_senn4kes_tzzzz
34C3_mo4r_sgln4kes_tzzzz
34C3_mo4r_sibn4kes_tzzzz
34C3_mo4r_smfn4kes_tzzzz
34C3_mo4r_sodn4kes_tzzzz
34C3_mo4r_sqzn4kes_tzzzz
34C3_mo4r_ssxn4kes_tzzzz
34C3_mo4r_syrn4kes_tzzzz
```

Here are our final candidates. We only have to find the correct one by testing their md5 hash.

```python
flag_sum = "5a76c600c2ca0f179b643a4fcd4bc7ac"

for flag in mo4r_test_flags:
    m = hashlib.md5(flag).hexdigest()
    #print m
    if (str(m) == flag_sum):
        print "FLAG: "+flag
```

However, when we test that - for a reason I don't understand - it seems that none of the hashes matches the one we're looking for. 
Still, when we test individually each potential flag in a terminal we find that :

```
$ echo "34C3_mo4r_schn4kes_tzzzz" | md5sum
5a76c600c2ca0f179b643a4fcd4bc7ac
```

And there is our flag : 34C3\_mo4r\_schn4kes\_tzzzz


EDIT : The reason was that `echo` inserts a '\n' at the end of the string, and we didn't insert one before testing the hashes in our script.

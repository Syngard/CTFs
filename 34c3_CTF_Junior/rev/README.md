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

Since the scrict is obfuscated, we should try at first to reorganize it to understand what is does.

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

So we are renaming some functions with non-readable names and then applying them to some values. Next, we have to rename everithing so as to understand what is actually happening here.

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

correct[[olol(*a) for a in zip(list(map(ord,data)), list(map(ord,data))[::-1])][::-1]==[160,155,208,160,190,215,237,134,210,126,212,222,224,238,128,240,164,213,183,192,162,178,163,162] and 'mo4r' in data and '34C3_' in data and data.split('_')[3] == 'tzzzz']()
```

The `correct` function will print if out password was correct depending on how the boolean expression given as a parameter will evaluate. We can break it down into three different conditions :

```python
olol(*a) for a in zip(list(map(ord,data)), list(map(ord,data))[::-1])][::-1] == [160,155,208,160,190,215,237,134,210,126,212,222,224,238,128,240,164,213,183,192,162,178,163,162]
```
The data encrypted with the `olol` function must be equal to this array. We'll explore later how exactlty is the encryption done.

```python
'mo4r' in data and '34C3_' in data and data.split('_')[3] == 'tzzzz'
```
The clear flag must contain the words "mo4r", "34C3\_" and "tzzzz". However, since we know the format of the flag, we can go a bit further. The flag will actually start with "34C3\_", and is likely to end with "\_tzzzz" (since "tzzzz" is extracted with `data.split('_')`, it must be preceded by an underscore). So our flag is in the format : "34C3\_" + ... + "\_tzzzz".


Now let's move on to the encryption part.

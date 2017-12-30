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

So we are renaming some functions with non-readable names and then applying them to some values. Next, we have to rename everything so as to understand what is actually happening here.

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

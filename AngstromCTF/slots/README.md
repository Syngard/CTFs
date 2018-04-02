# Slots challenge writeup

**Category:** Misc

**Description:**

> defund is building a casino empire. Break his [slot machine](./slots.py), which is running at web.angstromctf.com:3002. Note: connect with netcat or an equivalent tool.

## Solution write-up

When reading the python code, we see that the server only asks for an input and converts it to a float. When the amount of money left is 0 the connection is closed. Moreover, it is not a question of luck since we cannot actually win. The roulette will be relaunched as long as a winning output is given.


```python
while payout(line2):
    line2 = line()
```


Since the value has to be successfuly converted to a float and must not validate the check 
`if bet <= 0:`, I looked around to see what special values could be converted to float. I found that '-inf', '+inf' and 'Nan' worked. However, since the infinite values can be compared to other numbers, the checks wont be validated. But comparing 'Nan' and any other number will always return `False`, and we can get the flag with that.


```
$ nc web.angstromctf.com 3002
Welcome to Fruit Slots!
We've given you $10.00 on the house.
Once you're a high roller, we'll give you a flag.
You have $10.00.
Enter your bet: NaN
? : ? : ?
? : ? : ? ◀
? : ? : ?
You lost everything.
Wow, you're a high roller!
A flag: actf{fruity}
```

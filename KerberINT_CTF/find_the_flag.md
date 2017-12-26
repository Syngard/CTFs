# Find the flag challenge writeup

**Category:** Programming

**Description:**

> You have to submit the flag to XXX.XXX.XXX.XXX on port 3333 

## Solution write-up

Let's use netcat to see what the server actually gives us :   
$ nc XXX.XXX.XXX.XXX 3333
qwerty ( <= this is what I typed )
Wrong flag ! ( <= and this is what the server answered )


This doesn't help us much, as we obviously know that "qwerty" is not the flag. But we already know the first four characters of it, as they are always "CTF{". What if we give this to the server ?
$ nc XXX.XXX.XXX.XXX 3333
CTF{
You're on the right track !


That's interesting. And if we try to add another character ?   
$ nc XXX.XXX.XXX.XXX 3333
CTF{a
Wrong flag !


With that we can guess how to get the flag : we have to bruteforce it one character at the time. As always I did it with python beacause I find it easier. First thing we need is a module to establish a TCP connection to the server on the specified port. The [socket module](https://wiki.python.org/moin/TcpCommunication#Client) is super useful for that purpose. Let's write a TCP client that will send to the server whatever we feed it.

```python
HOST = 'XXX.XXX.XXX.XXX'
PORT = 3333

def tcp_client(msg):
    client = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
    client.connect(( HOST, PORT ))

    client.send(flag)
    return client.recv(4096)
```

Once we have our client, we need to check weather the string we send was correct or not. To do that we must compare the message returned by the server with the messages we already know it can send.

```python
def testResponse(response):
    return ("You're on the right track" in response)
```

Finally, we have to retrieve the flag character by character. We start with "CTF{" and we then add one character until we recieve a valid response. Once we do, we start over with the next one. We stop when we find the last character, which will be '}'


```python
flag = "CTF{"
while (flag[-1] != '}'):
        for i in ALPHA:
            time.sleep(0.1)
            DATA = flag + i
            response = tcp_client(DATA)

            if (testResponse(response)):
                flag += i
                #print flag
                break

```

I added a "time.sleep(0.1)" after a few tests because without it the answers recieved weren't synchronized with the characters being tested, resulting in a wrong character being selected and the loop never ending.

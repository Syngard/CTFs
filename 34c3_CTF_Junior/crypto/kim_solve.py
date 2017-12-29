import hashlib
import itertools
import string

ALPHA = string.ascii_letters + string.digits
tested_hash = "952bb2a215b032abe27d24296be099dc3334755c"
msg = "f=sample.gif"


for i in range(1,8):
    print i
    for string in itertools.product(ALPHA, repeat=i):
        test_secret = ''.join(string)
        test_hash = hashlib.sha1(test_secret + msg).hexdigest()

        if (test_hash == tested_hash):
            print test_secret


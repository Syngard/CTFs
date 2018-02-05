from hashlib import md5
import itertools

ALPHA = "0123456789abcde"

def foo(h, m):
    return md5(h.encode('utf-8') + m.encode('utf-8')).hexdigest()[:4]


def round(hl, m, hr):
    return foo(hl, m), foo(hr, m)


def fHash(hl, hr, M):
    message = list(map(''.join, zip(*[iter(M)] * 4)))
    for m in message:
        hl, hr = round(hl, m, hr)
    return hl + hr


if __name__ == '__main__':
    #print(fHash('7575', 'A8A8', '7368617269666374'))

    #old = ['7368','6172','6966','6374']
    hl4 = '260c'
    hr4 = '01da'

    new = ['0004','0006','0000','0223']

    hl3 = '4c8b'
    hr3 = '30d6'

    hl2 = '5e44'
    hr2 = '14e4'

    hl1 = 'e5ac'
    hr1 = '37db'

    hl0 = '7626'
    hr0 = '5267'

    print fHash(hl0, hr0, ''.join(new))

    """
    stop = False

    words = list(''.join(i) for i in itertools.product(ALPHA, repeat=4))

    for m2 in words:

        m = ''.join(m2)
        hr_col = False
        hl_col = False

        for h2 in words:
            h = ''.join(h2)

            hash_word = foo(h, m)

            #print "h = "+ h +" // m = "+ m +" // hash = "+ hash_word

            if (hash_word == hl1):
                print "hl collision found"
                print "hl0 = "+ h +" // m3 = "+ m
                hl_col = True

            if (hash_word == hr1):
                print "hr collision found"
                print "hr0 = "+ h +" // m3 = "+ m
                hr_col = True

            if (hl_col and hr_col):
                print 'Found !'
                stop = True
                break

        if (stop):
            break

    """

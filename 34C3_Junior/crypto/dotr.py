import random


def encrypt(msg, key):
    keylen = len(key)
    k = [x[1] for x in sorted(zip(key, range(keylen)))]

    m = ''
    for i in k:
        for j in range(i, len(msg), keylen):
            m += msg[j]

    return m



m = input()
while True:
    k = [random.randrange(256) for _ in range(16)]  # generate 2 keys
    if len(k) == len(set(k)):
        break

m = encrypt(m, k[:8])
m = encrypt(m, k[:8])

print(m)


encrypted_flag = "03_duCbr5e_i_rY_or cou14:L4G f313_Th_etrph00 Wh03UBl_oo?n07!_e"




#!/usr/bin/python
import hashlib
import sys

from itertools import cycle

ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_{}'
ciphertext = "xxhsmbgpogovffoqcrgkqneemgedoneeaeeihzgjkutjlvcpgnpjhjldlppqwgimdofcnrttz"

def encrypt(key, plaintext):
    """Encrypt the string and return the ciphertext"""
    pairs = zip(plaintext, cycle(key))
    result = ''

    for pair in pairs:
        (x,y)=pair
        #print(x,y)
        total = ALPHA.index(x) + ALPHA.index(y)
        result += ALPHA[total % 26]

    return result.lower()

def decrypt(key, plaintext):
    """Decrypt the string and return the ciphertext"""
    pairs = zip(plaintext, cycle(key))
    result = ''

    for pair in pairs:
        (x,y)=pair
        #print(x,y)
        total = ALPHA.index(x) - ALPHA.index(y)
        result += ALPHA[total % 26]

    return result.lower()

def find_key_letter(cipher_letter,clear_letter):
    key_letter = []
    v = False
    for i in ALPHA[:len(ALPHA) - 3]:
        if (encrypt(i, clear_letter) == cipher_letter):
            key_letter.append(i)
            if (len(key_letter) >= 2):
                if (key_letter[-1].lower() == key_letter[-2].lower()):
                    del key_letter[-1]
    return key_letter
    
    
def find_key(ciphertext,cleartext):
    key_list = ['']
    new_key_list = []
    for i in range(len(ciphertext)):
        key_letter_list = find_key_letter(ciphertext[i], cleartext[i])
        for key in  key_list:
            for letter in key_letter_list:
                new_key_list.append(key+letter)
        key_list = new_key_list[:]
        new_key_list = []
    return key_list


def break_cipher(cipher, key):
    clear = 'CTF{'
    for i in range(len(cipher)):
        for j in ALPHA:
            clear_test = clear + j
            cipher_test = encrypt(key, clear_test)
            if (cipher_test == cipher[:len(cipher_test)]):
                clear = clear_test
                print clear
    return clear

cleartext = "CTF{"
key = "V4ch3rcherL4ClefChezM3meSousL3Can4pe"

#break_cipher(ciphertext, key)

test_crypt = encrypt(key, "CTF{j_4i_p3rdu_la_cle_s0us_l3_c4nape}"+key)
print ciphertext 
print test_crypt


for i in range(len(ciphertext)):
    if (ciphertext[i] != test_crypt[i]):
        print str(i) + " >> " +key[i]
"""
k = len(key) +1
i = 36
cipher = ciphertext[i:i+k]
key_list = find_key(cipher, '}'+key)
for tmp_key in key_list:
    if (key.upper() in tmp_key):
        print str(i) + " >> " + tmp_key

for dec in range(4):
    for i in range(k+dec, len(ciphertext)-k+dec):
        possible_key_letters = find_key_letter(ciphertext[i], key[i%k])
        for j in possible_key_letters:
            print str(i)+" >> cipher_letter = "+key[i%k]+"//"+ciphertext[i]+" >> key_letter = "+str(j)
        


for i in ALPHA:
    for j in ALPHA:
        for k in ALPHA:
            for l in ALPHA:
                test_key = i+j+k+l
                test = encrypt(test_key, cleartext[:4])
                if (test == ciphertext[:4]):
                    print key


key=sys.argv[1]
plaintext=sys.argv[2]+key
cipher=encrypt(key,plaintext)
print(cipher)
"""

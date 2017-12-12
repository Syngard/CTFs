#! /bin/bash

secret=$(cat /dev/urandom | tr -dc 'a-z' | fold -w 5 | head -n 1)
flag=CTF\{$secret\}
echo $flag
echo -n $flag | md5sum

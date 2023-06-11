#!/bin/usr/env python3

import subprocess
import re
import os
import random
from inputimeout import inputimeout, TimeoutOccurred

NOT_ALLOWED = re.compile("[a-z*?.]")

def create_tmp_dir():
    random_name = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for x in range(32))
    dir_name = f'/tmp/{random_name}'
    os.mkdir(dir_name)
    return dir_name

def main(directory):
    print('Welcome to Crash Bash!')
    print('To get the flag, call /printflag.sh with the password!')
    print('Enter "q" to quit.')
    print('----------------------')
    do_run = True
    while do_run:
        try:
            inp = inputimeout(prompt='crashbash$ ', timeout=45)
            if 'q' == inp:
                print('Bye!')
                do_run = False
            elif NOT_ALLOWED.search(inp):
                print('Invalid character found, bash crashed!')
            else:
                try:
                    subprocess.run(['/bin/bash', '-c', inp], stdin=subprocess.PIPE, timeout=30, cwd=directory)
                except subprocess.TimeoutExpired:
                    print("Timeout")
        except:
            print('Timeout, bye!')
            do_run = False

if __name__ == '__main__':
    main(create_tmp_dir())
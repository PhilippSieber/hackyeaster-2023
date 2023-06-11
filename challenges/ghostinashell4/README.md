# solution
- ssh to the docker
- observe weird behavior of standard commands
- find it is made using aliases
- use `/bin/bash` to get a new bash without aliases
- find flag file in `/home/blinky/home/blinky/blinkyflag.fzip`
  - zip file
  - password-protected
  - brute-force and wordlist won't help
- in the original shell, list all aliases using `alias`
- find the following one:
  - `alias fzip='/usr/bin/zip -P "/bin/funzip"'`
  - file ending of flag file is a hint
  - password of the zip is **/bin/funzip**
- copy the zip file out of the server (which is read-only)
  - e.g. by using base64: `cat /home/blinky/home/blinky/blinkyflag.fzip | base64`
- use unzip and enter the password

# creation
echo "he2023{al1asses-4-fUn-and-pr0fit}" > flag.txt && zip -P bin_unzip -r blinky.zip flag.txt && rm flag.txt
FROM ubuntu:22.04

RUN apt update
RUN apt upgrade -y
RUN apt install -y curl
RUN apt remove gpg
RUN apt-get update -y
RUN apt-get install -y gnupg1
RUN curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall
RUN chmod +x msfinstall
RUN ./msfinstall

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /etc/security
COPY app/limits.conf .

WORKDIR /
RUN mkdir fl@gst0r3
COPY app/flag ./fl@gst0r3/

WORKDIR /home/ctf
COPY app/cheater .
COPY app/ynetd .
COPY app/create_shellcode.sh .
RUN chmod +x ynetd cheater create_shellcode.sh
RUN ./create_shellcode.sh

RUN chown -R root:root /home/ctf
RUN chmod o+rx /home/ctf
USER ctf
CMD ./ynetd ./cheater


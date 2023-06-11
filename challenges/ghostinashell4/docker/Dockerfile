FROM  panubo/sshd:1.3.0

RUN apk add util-linux zip openssl busybox-initscripts

RUN useradd -m blinky -s /bin/bash

RUN mkdir -p /home/blinky/blinky/
COPY files/blinky.zip /home/blinky/home/blinky/blinkyflag.fzip
COPY files/about.txt /home/blinky/about.txt
COPY files/rick.txt /home/blinky/flag.txt

COPY files/setup.sh /etc/entrypoint.d/
RUN chmod +x /etc/entrypoint.d/setup.sh

COPY files/alias.sh /etc/profile.d/alias.sh
RUN chmod +x /etc/profile.d/alias.sh
RUN source /etc/profile

COPY files/motd /etc/motd

EXPOSE 22

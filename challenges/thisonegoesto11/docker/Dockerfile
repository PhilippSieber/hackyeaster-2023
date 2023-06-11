FROM ubuntu:22.04

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /etc/security
COPY app/limits.conf .

WORKDIR /
RUN mkdir fl@gst0r3
COPY app/flag ./fl@gst0r3/

WORKDIR /home/ctf
COPY app/hell .
COPY app/ynetd .
RUN chmod +x ynetd hell

RUN chown -R root:root /home/ctf
RUN chmod o+rx /home/ctf
USER ctf
CMD ./ynetd ./hell


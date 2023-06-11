FROM ubuntu@sha256:daf3e62183e8aa9a56878a685ed26f3af3dd8c08c8fd11ef1c167a1aa9bd66a3

RUN apt-get update \
    && apt-get install -y xinetd build-essential libseccomp-dev \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /challenge
WORKDIR challenge

ADD app/main.c .
ADD app/seccomp-bpf.h .
RUN gcc main.c -O0 -lseccomp -fno-stack-protector -no-pie -o main # Disable optimizations just to be sure
RUN rm main.c

ADD app/FLAG .
ADD app/FLAG /
ADD app/xinetd.conf /etc/xinetd.d/conf

RUN useradd -M -d /challenge ctf

RUN chmod 644 FLAG \
    && chmod 644 /FLAG \
    && chmod 755 main \
    && chmod 644 /etc/xinetd.d/conf

EXPOSE 45678

CMD ["/usr/sbin/xinetd", "-dontfork"]

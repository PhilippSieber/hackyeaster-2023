FROM ubuntu@sha256:daf3e62183e8aa9a56878a685ed26f3af3dd8c08c8fd11ef1c167a1aa9bd66a3

RUN apt-get update \
    && apt-get install -y build-essential libseccomp-dev python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip
RUN pip3 install pwntools

RUN mkdir -p /challenge
WORKDIR challenge

ADD main .
ADD libc.so .
ADD exploit.py .

CMD ["python3", "/challenge/exploit.py"]

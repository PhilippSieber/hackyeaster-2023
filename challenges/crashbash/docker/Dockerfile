FROM ubuntu

RUN apt-get update && apt-get -y upgrade -y
RUN apt-get install -y xinetd python3 pip
RUN pip install inputimeout

RUN useradd -ms /bin/bash he

ADD app/xinetd.conf /etc/
ADD app/flag.txt /flag.txt
ADD app/run.sh /run.sh
ADD app/crashbash.py /crashbash.py
ADD app/printflag.sh /printflag.sh

RUN chown root:root /flag.txt
RUN chmod +x /run.sh
RUN chown root:root /printflag.sh && chmod 4555 /printflag.sh
RUN chmod 733 /tmp

EXPOSE 1337
ENTRYPOINT [ "xinetd", "-dontfork" ]

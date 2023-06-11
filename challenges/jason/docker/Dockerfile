FROM ubuntu

RUN apt-get update && apt-get -y upgrade -y
RUN apt-get install -y xinetd python3 pip jq
RUN pip install inputimeout

RUN useradd -ms /bin/bash he

ADD app/xinetd.conf /etc/
ADD app/data.json /data.json
ADD app/run.sh /run.sh
ADD app/jason.py /jason.py

RUN chown root:root /data.json
RUN chmod +x /run.sh
RUN chmod 733 /tmp

EXPOSE 1337
ENTRYPOINT [ "xinetd", "-dontfork" ]

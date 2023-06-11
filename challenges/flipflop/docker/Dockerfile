FROM python:3.8-slim-buster

COPY        ./app /app
COPY        ./flag.txt /flag.txt
WORKDIR     /app

RUN mkdir /app/uploads
RUN mkdir /app/converted
RUN apt update && apt upgrade -y 
RUN apt install imagemagick=8:6.9.10.23+dfsg-2.1+deb10u1 -y
RUN pip3 install -r requirements.txt

CMD [ "python3", "app.py"]

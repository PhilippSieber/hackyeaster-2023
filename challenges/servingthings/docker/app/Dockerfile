FROM python:3.10-slim
COPY . /app
WORKDIR /app
RUN mv /app/flag /flag

RUN apt-get update && apt-get upgrade -y && apt-get install -y wget procps net-tools

RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["controller.py"]

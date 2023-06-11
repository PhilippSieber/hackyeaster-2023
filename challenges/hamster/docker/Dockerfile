FROM golang:1.19.2-alpine3.16

WORKDIR /app
COPY ./app .

RUN go build -o main .
EXPOSE 1337

CMD ["./main"]
FROM golang:1.17.4-alpine3.14

WORKDIR /app
COPY ./app .

RUN go build -o main .
EXPOSE 2000

CMD ["./main"]
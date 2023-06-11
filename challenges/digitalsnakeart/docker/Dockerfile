FROM openjdk:8-jdk-alpine
COPY app/app.jar /app.jar
RUN mkdir /config/
COPY app/config/application.yml /config/application.yml
ENTRYPOINT ["java", "-jar", "/app.jar"]

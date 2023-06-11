#!/bin/bash
cd app
mvn package
cp target/digital*.jar ../../docker/app/app.jar
cd src/main/java
rm ../../../../../files/digitalsnakeart.zip
zip -r ../../../../../files/digitalsnakeart.zip .
cd - 
cd ..
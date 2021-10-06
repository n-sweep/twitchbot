FROM ubuntu:latest
WORKDIR /tmp/init_build

RUN apt-get update && apt-get install python3-pip git

COPY conf/requirements.txt ./
RUN pip3 install -r requirements.txt


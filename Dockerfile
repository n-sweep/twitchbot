FROM ubuntu:latest
WORKDIR /home/work
# WORKDIR /tmp/init_build

RUN apt-get update && apt-get -y install python3-pip git

RUN git clone https://github.com/n-sweep/twitchbot

RUN pip3 install -r twitchbot/conf/requirements.txt

COPY ./conf/config.json ./twitchbot/conf/

CMD ["python3", "twitchbot/run.py"]

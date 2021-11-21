FROM ubuntu:latest
WORKDIR /home/work

RUN apt-get update && apt-get -y install python3-pip git tmux

# RUN git clone https://github.com/n-sweep/twitchbot

RUN pip3 install -r twitchbot/conf/requirements.txt

COPY ./conf/config.json ./twitchbot/conf/

ENTRYPOINT ["python3", "twitchbot/run.py"]

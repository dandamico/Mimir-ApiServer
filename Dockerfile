FROM ubuntu:18.04

RUN apt-get update -y && apt-get install -y python3-pip 

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt
COPY . .

CMD python3 app.py
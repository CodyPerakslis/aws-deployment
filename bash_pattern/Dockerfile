FROM ubuntu:16.04
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3-pip nano
RUN pip3 install awscli boto3
RUN useradd -m aws
ENV HOME=/home/aws/
WORKDIR /home/aws/current/

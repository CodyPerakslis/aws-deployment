FROM python:3.7.0-alpine3.8
COPY requirements.txt /lib/requirements.txt
RUN pip3 install --upgrade pip && \
  pip3 install -r /lib/requirements.txt
COPY aws_lib /lib/aws_lib
COPY lib_files /lib/lib_files
WORKDIR /lib
ENV HOME /lib
ENTRYPOINT ["./aws_lib"]
CMD ["--help"]

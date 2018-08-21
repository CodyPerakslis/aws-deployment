FROM python:3.7.0-alpine3.8
RUN mkdir /aws
COPY requirements.txt /aws/requirements.txt
RUN pip3 install --upgrade pip && \
  pip3 install -r /aws/requirements.txt
COPY awslib /aws/awslib
COPY lib_files /aws/lib_files
WORKDIR /aws
ENV HOME /aws
ENTRYPOINT ["./awslib"]
CMD ["--help"]

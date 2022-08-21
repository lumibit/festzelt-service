# PYTHON DEPENDENCIES PACKER IMAGE
FROM amazonlinux:2.0.20220719.0

# https://techviewleo.com/how-to-install-python-on-amazon-linux/
RUN yum install -y amazon-linux-extras && \
    yum install -y zip && \
    amazon-linux-extras enable python3.8 && \
    yum install -y python3.8 && \
    yum clean all

COPY src/requirements.txt /requirements.txt

RUN pip3.8 install -r requirements.txt -t ./python && \
    zip -r python.zip ./python/
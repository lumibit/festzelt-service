FROM python:3.7-alpine

# add the requirements and install correct versions
ADD requirements.txt /requirements.txt

# install dependencies, add timezone information and cleanup
RUN \
apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev openssl-dev && \
apk add tzdata && cp /usr/share/zoneinfo/Europe/Berlin /etc/localtime && echo "Europe/Berlin" >/etc/timezone && \
pip install -r requirements.txt && \
apk del .build-deps gcc musl-dev libffi-dev openssl-dev

# add code
ADD /app /app

WORKDIR /app

CMD python3 main.py

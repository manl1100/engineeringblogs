FROM debian:jessie

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y upgrade
RUN set -x && apt-get update && DEBIAN_FRONTEND=noninteractive \
      apt-get install -y --no-install-recommends \
        ca-certificates \
        vim \
        curl \
        git \
        npm \
        python3 \
        python3-dev \
        python3-pip \
        build-essential \
        libmysqlclient-dev \
        libxml2-dev \ 
        libxslt-dev \
        libssl-dev \
        libffi-dev \
        g++




ADD . /code
WORKDIR /code

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]

CMD ["app.py"]

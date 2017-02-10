FROM debian:jessie

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y upgrade
RUN set -x && apt-get update && DEBIAN_FRONTEND=noninteractive \
      apt-get install -y --no-install-recommends \
        ca-certificates \
        vim \
        curl \
        git \
        npm \
        python-pip


ADD . /code
WORKDIR /code

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]

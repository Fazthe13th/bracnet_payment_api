FROM python:3.7-alpine3.12
LABEL "Auther"="Fazlul Haque"

ENV PYTHONUNBUFFERED 1

COPY ./requirments.txt /requirments.txt
RUN apk add --update --no-cache mariadb-client mariadb-connector-c linux-headers
RUN apk add --update --no-cache gcc libc-dev mariadb-dev

RUN apk add sudo
RUN pip install -r /requirments.txt
# RUN apk del .tmp-build-deps

RUN mkdir /bracnet_payment_api
WORKDIR /bracnet_payment_api
COPY ./bracnet_payment_api /bracnet_payment_api
COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web

RUN adduser -D faz13
RUN chown -R faz13:faz13 /vol
RUN chmod -R 755 /vol/web
USER faz13

# CMD ["/scripts/entrypoint.sh"]
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
# RUN python /bracnet_payment_api/bracnet_sc_bkash_api/manage.py makemigrations
RUN mkdir -p /bracnet_payment_api/static
RUN mkdir -p /bracnet_payment_api/media
RUN adduser -D user
RUN chown -R user:user /bracnet_payment_api
# RUN chmod -R 766 /bracnet_payment_api
RUN chmod -R 755 /bracnet_payment_api/static
RUN chmod -R 755 /bracnet_payment_api/media
USER user

# RUN adduser -D faz13
# RUN chown -R faz13:faz13 /vol
# RUN chmod -R 755 /vol/web
# USER faz13

# CMD ["/scripts/entrypoint.sh"]
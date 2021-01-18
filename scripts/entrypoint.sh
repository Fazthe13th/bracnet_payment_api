#!/bin/sh

# until ./manage.py migrate
# do
#     echo "Waiting for db to be ready..."
#     sleep 2
# done

# ./manage.py collectstatic --noinput

# gunicorn bracnet_sc_bkash_api.wsgi:application --bind 0.0.0.0:8000 --workers 4 --threads 4

set -e

python manage.py collectstatic --noinput

uwsgi --socket :8000 --master --enable-threads --module bracnet_sc_bkash_api.wsgi

ACME_CA_URI=https://acme-staging-v02.api.letsencrypt.org/directory
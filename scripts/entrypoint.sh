#!/bin/sh

set -e
python manage.py collectstatic --noinput
uwsgi --socket :443 --master --enable-threads --module bracnet_sc_bkash_api.wsgi
FROM jwilder/nginx-proxy
COPY vhost.d/default /etc/nginx/vhost.d/default
COPY custom.conf /etc/nginx/conf.d/custom.conf
# COPY ./uwsgi_params /etc/nginx/uwsgi_params
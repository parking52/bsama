FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y \
        python3-pip \
        libpython-dev

RUN pip3 install --upgrade pip setuptools

ADD . /package
RUN pip3 install /package
RUN rm -rf /package

COPY gunicorn_config.py .

ENV PYTHON_EGG_CACHE=/tmp/.python-eggs

EXPOSE 8080
CMD gunicorn \
    --bind 0.0.0.0:8080 \
    --config gunicorn_config.py \
    twocasas_backend_api.wsgi

#CMD twocasas-backend-api-application
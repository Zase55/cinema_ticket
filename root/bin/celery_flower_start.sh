#!/bin/bash

set -o errexit
set -o nounset

worker_ready() {
    celery -A django_celery.celery_instance inspect ping
}

until worker_ready; do
  >&2 echo 'Celery workers not available'
  sleep 1
done
>&2 echo 'Celery workers is available'

celery -A django_celery.celery_instance  \
    --broker="redis://redis:6379/0" \
    flower
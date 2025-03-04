#!/bin/bash

set -o errexit
set -o nounset

rm -f './celery_beat.pid'
celery -A django_celery.celery_instance beat -l INFO
#!/bin/bash

set -o errexit
set -o nounset

celery -A django_celery.celery_instance worker -l INFO
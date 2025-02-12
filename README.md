# root backend

## Requirements

- Docker
- Docker Compose
- [Python 3](https://www.python.org/)
- [pre-commit](https://pre-commit.com/)

## About

Template for django app

## Important

- Use localhost:8000, not 0.0.0.0

## Setup

Install the git hooks with:

```bash
python3 -m venv venv
source venv/bin/activate
pip install pre-commit
pip install ruff
pre-commit install
cp ./git-hook-commit-msg .git/hooks/commit-msg
```

Run the `install.sh` script:

```bash
./install.sh
# This project use directly docker
# If you want to try by your account you would need to create a new
# venv directory
```

Start Docker containers:

```bash
docker-compose up -d
```

Create a new superuser:

```bash
$ docker-compose run web python manage.py createsuperuser
```

Link to http://localhost:8000/web/admin/ and log in!

## Access Adminer in the browser

To access the database, go to http://localhost:8080/ and use the following credentials:

- System: PostgreSQL
- Server: database
- Username: root
- Password: root!
- Database: root

## Access Mongo Express in the browser

To access the database, go to http://localhost:8081/ and use the following credentials:

- Username: root
- Password: root!

## Access to the API

To access the API, go to http://localhost:8000/api/docs/

## Access to django admin

To access the API, go to http://localhost:8000/web/admin/

## Populate the database

To populate the database, run the following command:

```bash
docker-compose run web python manage.py populate
```

## Run tests

```bash
docker compose run web pytest
```

# Ecom FastAPI app

<p align="center">

<a href="https://www.python.org/downloads/release/python-390/" target="_blank">
    <img src="https://img.shields.io/badge/python-3.9-blue.svg" alt="python 3.9">
</a>
<a href="https://www.python.org/downloads/release/python-3100/" target="_blank">
    <img src="https://img.shields.io/badge/python-3.10-blue.svg" alt="python 3.10">
</a>
<a href="https://www.python.org/downloads/release/python-3110/" target="_blank">
    <img src="https://img.shields.io/badge/python-3.11-blue.svg" alt="python 3.11">
</a>
<a href="https://github.com/kimdoanh89/ecom/actions?query=workflow%3ATest" target="_blank">
    <img src="https://github.com/kimdoanh89/ecom/workflows/Test/badge.svg" alt="Test">
</a>
<a href="https://codecov.io/gh/kimdoanh89/ecom" target="_blank">
    <img src="https://codecov.io/gh/kimdoanh89/ecom/branch/master/graph/badge.svg?token=I05R6KB0ZV" alt="Coverage">
</a>
</p>

This is tutorial from Pycharm. [Ref](https://www.jetbrains.com/pycharm/guide/tutorials/fastapi-aws-kubernetes/introduction/).

<a name="contents"></a>
## Contents
1. [Contents](#contents)
2. [Setup](#setup)
3. [Migration](#migration)

 
<a name="setup"></a>
## Setup
- Install PostgreSQL: [ref](https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-22-04-quickstart).
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo -u postgres createuser --interactive  # create user name `doanhluong`
# Login to postgres
sudo -i -u postgres psql
# Alter password
ALTER USER doanhluong WITH PASSWORD 'doanhluong123';
```
- Install SQLAlchemy
```bash
sudo apt-get install libpq-dev python3-dev build-essential
poetry add SQLAlchemy psycopg2 alembic "passlib[argon2]" email-validator
poetry add mypy flake8 black isort "coverage[toml]" pytest --dev
```
<a name="migration"></a>
## Migration
- Migration with Alembic
- Init alembic for migration: `alembic init alembic`
- Revise: `alembic revision --autogenerate`
- Run the migration: `alembic upgrade head`
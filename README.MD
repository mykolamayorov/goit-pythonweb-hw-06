# GOIT Python Web HW 06

## Description

This project is a PostgreSQL database using SQLAlchemy ORM with Alembic migrations. It includes models for students, groups, teachers, subjects, and grades.

## Features

- SQLAlchemy ORM models
- Alembic migrations
- Faker database seeding
- 10 SQLAlchemy analytical queries

## Run project

pip install -r requirements.txt  
alembic upgrade head  
python seed.py  
python my_select.py

## Database (Docker)

docker run --name goit-postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres

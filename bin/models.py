#!/usr/bin/env python
from dotenv import load_dotenv, dotenv_values
import os


# flask-sqlacodegen --flask --notables --outfile models.py postgresql://miya_db:root@192.169.201.1:5432/db


def generate_models():
    load_dotenv()
    db_url = dotenv_values().get('SQLALCHEMY_DATABASE_URI')
    os.system(f'flask-sqlacodegen --flask --notables {db_url}')


if __name__ == '__main__':
    generate_models()

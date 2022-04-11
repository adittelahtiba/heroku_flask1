from os import environ 

SECRET_KEY = environ.get('SECRET_KEY')
API_KEY = environ.get('API_KEY')
DBSERVER = environ.get('DBSERVER')
DBPORT = environ.get('DBPORT')
DBMS = environ.get('DBMS')
DB_USER = environ.get('DB_USER')
DATABASE = environ.get('DATABASE')
DB_URI = environ.get('DB_URI')
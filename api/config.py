import os

class DevelopmentConfig:

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8mb4'.format(**{
        'user': os.getenv('MYSQL_USER', 'mysql_user'),
        'password': os.getenv('MYSQL_PASSWORD', 'pass'),
        'host': os.getenv('MYSQL_HOST', 'localhost'),
        'database': os.getenv('MYSQL_DATABASE', 'mysql_db')
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

Config = DevelopmentConfig
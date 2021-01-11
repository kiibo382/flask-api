import os

class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8mb4'.format(**{
        'user': 'mysql_user',
        'password': 'pass',
        'host': '172.22.0.3',
        'database': os.getenv('MYSQL_DATABASE', 'mysql_db')
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

Config = DevelopmentConfig
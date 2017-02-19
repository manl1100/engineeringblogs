import os


class BaseConfig(object):
    DB_USER = os.environ['MYSQL_USER']
    DB_PASS = os.environ['MYSQL_PASSWORD']
    DB_SERVICE = os.environ['DB_SERVICE']
    DB_PORT = os.environ['DB_PORT']
    DB_NAME = os.environ['MYSQL_DATABASE']
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://{0}:{1}@{2}:{3}/{4}'.format(
        DB_USER, DB_PASS, DB_SERVICE, DB_PORT, DB_NAME
    )

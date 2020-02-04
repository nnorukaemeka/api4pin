import os

base_dir = os.path.abspath(os.path.dirname(__file__))
postgres_local_base = 'postgresql://postgres:123456@localhost/'
database_name = ''

# postgres_local_base = 'mysql://root:Olu1989!@@localhost/api4pin'

class BaseConfig:
    """
    Base application configuration
    """
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_strong_key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MONGO_URI = 'mongodb+srv://nnorukaemeka:oluchukwu.1@cluster0-s5htx.mongodb.net/test?retryWrites=true&w=majority'


class DevelopmentConfig(BaseConfig):
    """
    Development application configuration
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', postgres_local_base + database_name)




class ProductionConfig(BaseConfig):
    """
    Production application configuration
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', postgres_local_base + database_name)


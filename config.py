import os
from dotenv import load_dotenv
import uuid

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", uuid.uuid4().hex)
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False

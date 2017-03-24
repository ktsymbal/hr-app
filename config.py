import os

base_dir = os.path.abspath('./')

DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'test.sqlite')
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
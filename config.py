import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
  DEBUG = True
  ENV = 'development'
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'aqui-ninguem-suspeita'
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir + '/app.db')
  SQLALCHEMY_TRACK_MODIFICATIONS = False


import os.path
basedir = os.path.abspath(os.path.dirname(__file__))



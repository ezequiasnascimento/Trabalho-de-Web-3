from flask import Flask
from flask_ngrok import run_with_ngrok
from flask_bootstrap import Bootstrap
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager



app = Flask(__name__)
app.config.from_object(Config)

run_with_ngrok(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager()
login.init_app(app)
login.login_view = 'login'

import logging
from logging.handlers import RotatingFileHandler
import os

if not os.path.exists("logs"):
  os.mkdir("logs")

arquivo_handler = RotatingFileHandler("logs/erros.log", maxBytes=100000, backupCount=10)
arquivo_handler.setFormatter(logging.Formatter(
  "%(asctime)s %(levelname)s: %(message)s [em %(pathname)s: %(lineno)d]"))
arquivo_handler.setLevel(logging.WARNING)
app.logger.addHandler(arquivo_handler)
app.logger.setLevel(logging.INFO)
app.logger.info("Aplicação inicializada!")


from app.controllers import default
from app.models import carro
from app.models import comentario
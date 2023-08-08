from flask import Flask
from models import db, login
import config

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = config.db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = config.secret_key

db.init_app(app)
login.init_app(app)

with app.app_context():
    db.create_all()

import pollbooth

import enum

from flask_sqlalchemy import BaseQuery, SQLAlchemy
from sqlalchemy import func
from sqlalchemy.event import listens_for
from sqlalchemy.types import TypeDecorator

from flask_login import LoginManager, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import sqlalchemy
import json

db = SQLAlchemy()
login = LoginManager()


@login.user_loader
def load_user(id):
    return User.query.get(int(id))



class User(db.Model, UserMixin):
    # Used to login to the Admin Panel
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    username = db.Column(db.String(100))
    password_hash = db.Column(db.String)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@listens_for(User.__table__, "after_create")
def create_default_user(target, connection, **kw):
    """Adds a default user to The Underground.
    By default, we assume admin:admin."""
    table = User.__table__
    connection.execute(
        table.insert().values(
            username="admin",
            password_hash=generate_password_hash("admin"),
        )
    )


class Questions(db.Model):
    question_id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    content_japanese = db.Column(db.String)
    content_english = db.Column(db.String)
    content_german = db.Column(db.String)
    content_french = db.Column(db.String)
    content_spanish = db.Column(db.String)
    content_italian = db.Column(db.String)
    content_dutch = db.Column(db.String)
    content_portuguese = db.Column(db.String)
    content_french_canada = db.Column(db.String)
    content_catalan = db.Column(db.String)
    content_russian = db.Column(db.String)
    choice1_japanese = db.Column(db.String)
    choice1_english = db.Column(db.String)
    choice1_german = db.Column(db.String)
    choice1_french = db.Column(db.String)
    choice1_spanish = db.Column(db.String)
    choice1_italian = db.Column(db.String)
    choice1_dutch = db.Column(db.String)
    choice1_portuguese = db.Column(db.String)
    choice1_french_canada = db.Column(db.String)
    choice1_catalan = db.Column(db.String)
    choice1_russian = db.Column(db.String)
    choice2_japanese = db.Column(db.String)
    choice2_english = db.Column(db.String)
    choice2_german = db.Column(db.String)
    choice2_french = db.Column(db.String)
    choice2_spanish = db.Column(db.String)
    choice2_italian = db.Column(db.String)
    choice2_dutch = db.Column(db.String)
    choice2_portuguese = db.Column(db.String)
    choice2_french_canada = db.Column(db.String)
    choice2_catalan = db.Column(db.String)
    choice2_russian = db.Column(db.String)
    worldwide = db.Column(db.Boolean)
    start_date = db.Column(db.BigInteger)
    end_date = db.Column(db.BigInteger)


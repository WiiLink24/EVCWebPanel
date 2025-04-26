from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Questions(db.Model):
    question_id = db.Column(
        db.Integer, primary_key=True, unique=True, autoincrement=True
    )
    content_english = db.Column(db.String)
    content_german = db.Column(db.String)
    content_french = db.Column(db.String)
    content_spanish = db.Column(db.String)
    content_italian = db.Column(db.String)
    content_dutch = db.Column(db.String)
    content_portuguese = db.Column(db.String)
    content_french_canada = db.Column(db.String)
    choice1_english = db.Column(db.String)
    choice1_german = db.Column(db.String)
    choice1_french = db.Column(db.String)
    choice1_spanish = db.Column(db.String)
    choice1_italian = db.Column(db.String)
    choice1_dutch = db.Column(db.String)
    choice1_portuguese = db.Column(db.String)
    choice1_french_canada = db.Column(db.String)
    choice2_english = db.Column(db.String)
    choice2_german = db.Column(db.String)
    choice2_french = db.Column(db.String)
    choice2_spanish = db.Column(db.String)
    choice2_italian = db.Column(db.String)
    choice2_dutch = db.Column(db.String)
    choice2_portuguese = db.Column(db.String)
    choice2_french_canada = db.Column(db.String)
    type = db.Column(db.String)
    date = db.Column(db.Date)
    category = db.Column(db.SmallInteger)

class Suggestions(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country_code = db.Column(db.Integer, nullable=False)
    region_code = db.Column(db.Integer, nullable=False)
    language_code = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String, nullable=False)
    choice1 = db.Column(db.String, nullable=False)
    choice2 = db.Column(db.String, nullable=False)
    wii_no = db.Column(db.BigInteger, nullable=False)
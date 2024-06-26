from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    BooleanField,
    IntegerField
)
from wtforms.validators import DataRequired, ValidationError

class QuestionForm(FlaskForm):
    content_japanese = StringField("Japanese Question", validators=[DataRequired()])
    content_english = StringField("English Question", validators=[DataRequired()])
    content_german = StringField("German Question", validators=[DataRequired()])
    content_french = StringField("French Question", validators=[DataRequired()])
    content_spanish = StringField("Spanish Question", validators=[DataRequired()])
    content_italian = StringField("Italian Question", validators=[DataRequired()])
    content_dutch = StringField("Dutch Question", validators=[DataRequired()])
    content_portuguese = StringField("Portuguese Question", validators=[DataRequired()])
    content_catalan = StringField("Catalan Question", validators=[DataRequired()])
    content_russian = StringField("Russian Question", validators=[DataRequired()])
    content_french_canada = StringField("French Canadian Question", validators=[DataRequired()])
    choice1_japanese = StringField("Japanese Choice 1", validators=[DataRequired()])
    choice1_english = StringField("English Choice 1", validators=[DataRequired()])
    choice1_german = StringField("German Choice 1", validators=[DataRequired()])
    choice1_french = StringField("French Choice 1", validators=[DataRequired()])
    choice1_spanish = StringField("Spanish Choice 1", validators=[DataRequired()])
    choice1_italian = StringField("Italian Choice 1", validators=[DataRequired()])
    choice1_dutch = StringField("Dutch Choice 1", validators=[DataRequired()])
    choice1_portuguese = StringField("Portuguese Choice 1", validators=[DataRequired()])
    choice1_french_canada = StringField("French Canadian Choice 1", validators=[DataRequired()])
    choice1_catalan = StringField("Catalan Choice 1", validators=[DataRequired()])
    choice1_russian = StringField("Russian Choice 1", validators=[DataRequired()])
    choice2_japanese = StringField("Japanese Choice 2", validators=[DataRequired()])
    choice2_english = StringField("English Choice 2", validators=[DataRequired()])
    choice2_german = StringField("German Choice 2", validators=[DataRequired()])
    choice2_french = StringField("French Choice 2", validators=[DataRequired()])
    choice2_spanish = StringField("Spanish Choice 2", validators=[DataRequired()])
    choice2_italian = StringField("Italian Choice 2", validators=[DataRequired()])
    choice2_dutch = StringField("Dutch Choice 2", validators=[DataRequired()])
    choice2_portuguese = StringField("Portuguese Choice 2", validators=[DataRequired()])
    choice2_french_canada = StringField("French Canadian Choice 2", validators=[DataRequired()])
    choice2_catalan = StringField("Catalan Choice 2", validators=[DataRequired()])
    choice2_russian = StringField("Russian Choice 2", validators=[DataRequired()])
    worldwide = BooleanField("Worldwide Question")
    start_date = IntegerField("Start Date", validators=[DataRequired()])
    submit = SubmitField("Add")


class DeleteForm(FlaskForm):
    given_id = StringField("ID", validators=[DataRequired()])
    submit = SubmitField("Delete")

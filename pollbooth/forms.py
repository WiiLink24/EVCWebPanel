from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    PasswordField,
    BooleanField,
    IntegerField
)
from wtforms.validators import DataRequired, ValidationError


class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
    submit = SubmitField("Enter the underground")


class NewUserForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password1 = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField("Confirm Password", validators=[DataRequired()])
    upload = SubmitField("Complete")

    def validate_password1(self, _):
        if self.password1.data != self.password2.data:
            return ValidationError("New passwords must be the same")


class ChangePasswordForm(FlaskForm):
    current_password = PasswordField("Password", validators=[DataRequired()])
    new_password = PasswordField("New Password", validators=[DataRequired()])
    new_password_confirmation = PasswordField(
        "Confirm New Password", validators=[DataRequired()]
    )
    complete = SubmitField("Complete")

    def validate_current_password(self, _):
        if self.current_password.data == self.new_password.data:
            return ValidationError("New password cannot be the same as current!")

    def validate_new_password(self, _):
        if self.new_password.data != self.new_password_confirmation.data:
            return ValidationError("New passwords must be the same")


class QuestionForm(FlaskForm):
    content_japanese = StringField("Japanese Question", validators=[DataRequired()])
    content_english = StringField("English Question", validators=[DataRequired()])
    content_german = StringField("German Question", validators=[DataRequired()])
    content_french = StringField("French Question", validators=[DataRequired()])
    content_spanish = StringField("Spanish Question", validators=[DataRequired()])
    content_italian = StringField("Italian Question", validators=[DataRequired()])
    content_dutch = StringField("Dutch Question", validators=[DataRequired()])
    content_portuguese = StringField("Portuguese Question", validators=[DataRequired()])
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
    choice2_japanese = StringField("Japanese Choice 2", validators=[DataRequired()])
    choice2_english = StringField("English Choice 2", validators=[DataRequired()])
    choice2_german = StringField("German Choice 2", validators=[DataRequired()])
    choice2_french = StringField("French Choice 2", validators=[DataRequired()])
    choice2_spanish = StringField("Spanish Choice 2", validators=[DataRequired()])
    choice2_italian = StringField("Italian Choice 2", validators=[DataRequired()])
    choice2_dutch = StringField("Dutch Choice 2", validators=[DataRequired()])
    choice2_portuguese = StringField("Portuguese Choice 2", validators=[DataRequired()])
    choice2_french_canada = StringField("French Canadian Choice 2", validators=[DataRequired()])
    worldwide = BooleanField("Worldwide Question")
    start_date = IntegerField("Start Date", validators=[DataRequired()])
    submit = SubmitField("Add")


class DeleteForm(FlaskForm):
    given_id = StringField("ID", validators=[DataRequired()])
    submit = SubmitField("Delete")

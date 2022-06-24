from wtforms.validators import InputRequired, Email, EqualTo
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')


class SignUpForm(FlaskForm):
    full_name = StringField('Full name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[
        InputRequired()
    ])
    confirm_password = PasswordField('Confirm password', validators=[InputRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Sign up')

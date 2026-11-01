
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class RegistrationForm(FlaskForm):

    # Username
    username = StringField(
        "Username",
        validators=[
            DataRequired(),
            Length(min=3, max=80)
        ]
    )

    # Email address
    email = StringField(
        "Email Address",
        validators=[
            DataRequired(),
            Email(),
            Length(max=120)
        ]
    )

    # Password
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=8, max=128)
        ]
    )

    # Confirm password
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match.")
        ]
    )

    # Submit button
    submit = SubmitField("Create Account")


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):

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
            DataRequired()
        ]
    )

    # Submit button
    submit = SubmitField("Log In")

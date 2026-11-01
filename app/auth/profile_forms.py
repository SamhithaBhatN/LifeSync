
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class ProfileUpdateForm(FlaskForm):

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

    # Submit button
    submit = SubmitField("Update Profile")

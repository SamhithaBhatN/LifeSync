from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class ChangePasswordForm(FlaskForm):

    # Current password
    current_password = PasswordField(
        "Current Password",
        validators=[
            DataRequired()
        ]
    )

    # New password
    new_password = PasswordField(
        "New Password",
        validators=[
            DataRequired(),
            Length(min=8, max=128)
        ]
    )

    # Confirm new password
    confirm_new_password = PasswordField(
        "Confirm New Password",
        validators=[
            DataRequired(),
            EqualTo(
                "new_password",
                message="New passwords must match."
            )
        ]
    )

    # Submit button
    submit = SubmitField("Change Password")
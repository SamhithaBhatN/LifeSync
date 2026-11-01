
from flask import render_template, redirect, url_for, flash
from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user
)
from app.auth.password_forms import ChangePasswordForm
from app.auth import auth
from app.auth.forms import RegistrationForm
from app.auth.login_forms import LoginForm
from app.extensions import db
from app.models import User


@auth.route("/register", methods=["GET", "POST"])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():

        email = form.email.data.strip().lower()

        # Check whether the email already exists
        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash("An account with this email already exists.", "warning")
            return render_template("auth/register.html", form=form)

        # Create a new user
        user = User(
            username=form.username.data.strip(),
            email=email
        )

        # Hash the password
        user.set_password(form.password.data)

        # Save the user to the database
        db.session.add(user)
        db.session.commit()

        flash(
            "Your LifeSync account has been created successfully!",
            "success"
        )

        return redirect(url_for("auth.register"))

    return render_template("auth/register.html", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        email = form.email.data.strip().lower()

        # Find the registered user
        user = User.query.filter_by(email=email).first()

        # Verify user credentials
        if user and user.check_password(form.password.data):

            # Create authenticated session
            login_user(user)

            flash("Welcome back to LifeSync!", "success")

            return redirect(url_for("main.home"))

        else:
            flash(
                "Invalid email address or password.",
                "danger"
            )

    return render_template("auth/login.html", form=form)


@auth.route("/logout")
@login_required
def logout():

    # End the authenticated user session
    logout_user()

    flash("You have successfully logged out of LifeSync.", "success")

    return redirect(url_for("auth.login"))

@auth.route("/change-password", methods=["GET", "POST"])
@login_required
def change_password():

    form = ChangePasswordForm()

    if form.validate_on_submit():

        # Verify the current password
        if not current_user.check_password(form.current_password.data):

            flash(
                "Your current password is incorrect.",
                "danger"
            )

        else:
            # Set the new password securely
            current_user.set_password(form.new_password.data)

            # Save the updated password
            db.session.commit()

            flash(
                "Your password has been changed successfully!",
                "success"
            )

            return redirect(url_for("auth.change_password"))

    return render_template(
        "auth/change_password.html",
        form=form
    )
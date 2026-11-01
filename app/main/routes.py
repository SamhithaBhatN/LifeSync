from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from app.main import main
from app.auth.profile_forms import ProfileUpdateForm
from app.models import User
from app.extensions import db


@main.route('/')
def home():
    return render_template('index.html')


@main.route('/dashboard')
@login_required
def dashboard():

    return render_template(
        'dashboard/index.html',
        user=current_user
    )


@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():

    form = ProfileUpdateForm()

    if form.validate_on_submit():

        username = form.username.data.strip()
        email = form.email.data.strip().lower()

        # Check whether another user already uses this email
        existing_user = User.query.filter(
            User.email == email,
            User.id != current_user.id
        ).first()

        if existing_user:
            flash(
                "This email address is already registered.",
                "warning"
            )

        else:
            # Update the current user's information
            current_user.username = username
            current_user.email = email

            db.session.commit()

            flash(
                "Your profile has been updated successfully!",
                "success"
            )

            return redirect(url_for('main.profile'))

    # Display the current profile information
    if not form.is_submitted():
        form.username.data = current_user.username
        form.email.data = current_user.email

    return render_template(
        'dashboard/profile.html',
        user=current_user,
        form=form
    )
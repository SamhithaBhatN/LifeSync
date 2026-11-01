
from flask import Flask

from config import Config
from app.extensions import db, migrate, login_manager, csrf, babel
from app.main import main
from app.models import User
from app.auth import auth

def create_app(config_class=Config):
    app = Flask(__name__)

    # Load application configuration
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    
    # Configure Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        try:
            return db.session.get(User, int(user_id))
        except (TypeError, ValueError):
            return None

    csrf.init_app(app)
    babel.init_app(app)

    # Register Blueprints
    app.register_blueprint(main)
    app.register_blueprint(auth, url_prefix="/auth")

    return app

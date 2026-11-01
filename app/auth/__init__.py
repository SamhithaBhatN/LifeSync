
from flask import Blueprint

# Create the authentication Blueprint
auth = Blueprint("auth", __name__)

# Import authentication routes
from app.auth import routes
import logging
import os
import gunicorn
from flask import Flask, request, current_app

from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
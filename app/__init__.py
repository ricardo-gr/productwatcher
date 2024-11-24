from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    # Load configurations from config.py
    app.config.from_object("config.Config")

    # Register blueprints (routes)
    with app.app_context():
        from .routes import main
        app.register_blueprint(main)

    return app

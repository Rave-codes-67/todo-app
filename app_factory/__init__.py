from flask import Flask
from dotenv import load_dotenv
from datetime import timedelta
import os


def create_app(secret_key):
    app = Flask(__name__,
                template_folder='../templates',
                static_folder='../static')

    load_dotenv()

    app.secret_key = secret_key
    app.permanent_session_lifetime = timedelta(days=30)

    from app_factory.routes.main import main_bp
    from app_factory.routes.accounts import accs_bp
    from app_factory.routes.todo import todo_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(accs_bp)
    app.register_blueprint(todo_bp)

    return app
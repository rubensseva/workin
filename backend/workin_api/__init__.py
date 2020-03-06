from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    db.init_app(app)

    with app.app_context():
        from .shared import auth_helpers
        from .user import user_router
        from .workout import workout_router
        from .workout_entry import workout_entry_router
        from .workout_plan import workout_plan_router

        # Create tables for our models
        db.create_all()

        return app

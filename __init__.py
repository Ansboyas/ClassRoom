from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import student_api, teacher_api, principal_api
    app.register_blueprint(student_api.bp)
    app.register_blueprint(teacher_api.bp)
    app.register_blueprint(principal_api.bp)

    return app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from . import auth
import os
import config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
 
    if app.config['ENV'] == 'Production':
        app.config.from_object(config.ProductionConfig)
    elif test_config is None:
        app.config.from_object(config.DevelopmentConfig)
    else:
        app.config.from_object(config.TestingConfig)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from . import models
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Blueprints
    app.register_blueprint(auth.bp)

    @app.route("/test")
    def test():
        return "Working..."
    @app.route("/fail")
    def fail():
        return "Failed"
    return app
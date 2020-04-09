from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import config

db = SQLAlchemy()
migrate = Migrate()


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

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/test")
    def test():
        return "Working..."
    
    return app
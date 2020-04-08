from flask import Flask
import os
import config

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config.DevelopmentConfig")

    if app.config['ENV'] == 'Production':
        app.config.from_object(config.ProductionConfig)

    elif test_config is None:
        app.config.from_object(config.DevelopmentConfig)
    else:
        app.config.from_object(config.TestingConfig)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/test")
    def test():
        return "Working..."
    
    return app
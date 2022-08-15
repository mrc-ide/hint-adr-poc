from flask import Flask, jsonify
from app.config import TestingConfig, DevelopmentConfig, ProductionConfig
import os
from app.exceptions import AuthError
# blueprints
from app.errors.handlers import errors
from app.home.routes import home


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

app.register_blueprint(errors)
app.register_blueprint(home)


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig if os.environ.get(
        "PRODUCTION").lower() == 'true' else DevelopmentConfig)

    from app.errors.handlers import errors
    from app.home.routes import home

    app.register_blueprint(errors)
    app.register_blueprint(home)

    return app


@app.errorhandler(AuthError)
def authorization_error(e):
    response = jsonify(e.error)
    response.status_code = e.status_code
    return response

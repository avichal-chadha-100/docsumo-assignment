"""The app module, containing the app factory function."""
from flask import Flask
import logging
import sys
from docsumo.exceptions import InvalidUsage
from docsumo.extensions import cors
from docsumo.api import views as api_views
from flask_restful import Api
from flask_bootstrap import Bootstrap


def create_app(config_object="docsumo.config.settings"):
    app = Flask(__name__.split('.')[0])
    app.url_map.strict_slashes = False
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    pass


def register_blueprints(app):
    """Register Flask blueprints."""
    origins = app.config.get('CORS_ORIGIN_WHITELIST', '*')
    cors.init_app(api_views.blueprint, origins=origins)

    app.register_blueprint(api_views.blueprint)


def register_errorhandlers(app):
    def errorhandler(error):
        response = error.to_json()
        response.status_code = error.status_code
        return response

    app.errorhandler(InvalidUsage)(errorhandler)

import settings
import os
from flask_restx import Api
from flask import Blueprint
from flask import Flask
from flask_mail import Mail, Message
from werkzeug.middleware.proxy_fix import  ProxyFix

global app
global mail_app

api = Api(version='1.0', title='Restaurant Chat bot', description='Api to handle restaurant bot')


def create_app():
    print('Entering initialize app()')
    global app
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.debug = settings.FLASK_DEBUG
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP

    blueprint = Blueprint(settings.APP_API_CONTEXT, __name__, url_prefix=settings.FLASK_APP_CONTEXT)

    api.init_app(blueprint, doc=settings.FLASK_APP_CONTEXT)
    app.register_blueprint(blueprint)

    return app, api


def create_mail():
    print('Entering initialize app()')
    global mail_app
    mail_app = Flask(__name__)

    # configuration of mail
    mail_app.config['MAIL_SERVER'] = settings.MAIL_SERVER
    mail_app.config['MAIL_PORT'] = settings.MAIL_PORT
    mail_app.config['MAIL_USERNAME'] = settings.MAIL_USERNAME
    mail_app.config['MAIL_PASSWORD'] = settings.MAIL_PASSWORD
    mail_app.config['MAIL_USE_TLS'] = settings.MAIL_USE_TLS
    mail_app.config['MAIL_USE_SSL'] = settings.MAIL_USE_SSL

    mail = Mail(mail_app)

    return mail

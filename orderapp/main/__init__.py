from flask import Flask, Blueprint
from flask_swagger_ui import get_swaggerui_blueprint
from flask_restplus import Api, Resource, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

from orderapp.db import db
from orderapp.reference_data_load import init_db

from .controller.order_controller import api as order_ns

import os, markdown

order_blueprint = Blueprint('api', __name__)

api = Api(order_blueprint, version='1.0', title='Fruit Orders API',
    description='Fruit Orders',
)

api.add_namespace(order_ns, path='/order')

#Create an instance of Flask
app = Flask(__name__)
app.register_blueprint(order_blueprint)

#SQLAlchemy config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orderservice.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['RESTPLUS_MASK_SWAGGER'] = False

db.init_app(app)



### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yaml'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Fruit Order System"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###

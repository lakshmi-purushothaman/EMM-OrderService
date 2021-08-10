from flask import Flask, Blueprint
from flask_swagger_ui import get_swaggerui_blueprint
from flask_restplus import Api, Resource, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

from orderapp.db import db
from orderapp.main.controller.order_controller import api as order_ns

from orderapp.main.controller.offer_controller import offerapi as offer_ns
import os, markdown

#Create an instance of Flask
app = Flask(__name__)

#Flask Blueprint config for order
order_blueprint = Blueprint('api', __name__, url_prefix='/order')
api = Api(order_blueprint, version='1.0', title='Fruit Orders API',
    description='Fruit Orders',
)
api.add_namespace(order_ns)


#Flask Blueprint config for offer
offer_blueprint = Blueprint('offerapi', __name__, url_prefix='/offer')
offerapi = Api(offer_blueprint, version='1.0', title='Fruit Offers API',
    description='Fruit Offers',
)
offerapi.add_namespace(offer_ns)

#App registering with blueprint
app.register_blueprint(order_blueprint)
app.register_blueprint(offer_blueprint)

#SQLAlchemy config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orderservice.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['RESTPLUS_MASK_SWAGGER'] = False

#Initialize app
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

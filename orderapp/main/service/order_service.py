import uuid, datetime
import logging

from orderapp.main.model.order_dto import OrderDto
from orderapp.main.model.order_model import Order
from orderapp.main.model.product_model import Product
from orderapp.main.model.product_catalog_model import ProductCatalog
from orderapp.main.model.offer_model import Offer

from orderapp.db import db

from sqlalchemy.exc import SQLAlchemyError

#Logging configurations
logging.basicConfig(level=logging.DEBUG)

product = OrderDto.product

def save_order(order_request):
    order = lambda: None
    try:
        if order_request != None:
            order_id = str(uuid.uuid4())
            products = []
            product_request = order_request['products']
            
            if  product_request != None:
                catalogs =  get_all_product_catalog()
                for product in product_request:
                    product_type=product['producttype']
                    for catalog in catalogs:
                        if catalog.producttype == product_type:
                            product = Product(
                                producttype=product_type,
                                units=product['units'],
                                discountedunits=calculate_total_product_units_offer(requested_product_unit=product['units'],catalog_id=catalog.catalog_id),
                                order_id=order_id,
                                catalog_id=catalog.catalog_id
                            )
                            products.append(product)

            order = Order(
                username=order_request['username'],
                orderid=order_id,
                orderdate=datetime.datetime.utcnow(),
                totalordercost=calculate_total_order_cost(products),
                products=products
            )
            save_changes(order)
        else:
            order = None
    except KeyError as exp:
        raise KeyError
        logging.error("Key missing", exc_info=True)
    except SQLAlchemyError as exp:
        raise SQLAlchemyError
        logging.error("DB Error", exc_info=True)
    except Exception as exp:
        logging.error("Error occured while saving the order", exc_info=True)
    return order

def calculate_total_order_cost(products):
    try:
        order_cost=0
        if products!=None:
            for product in products:
                catalog = get_product_catalog_for_id(product.catalog_id)
                order_cost = order_cost + catalog.cost*product.units
                logging.info(order_cost)
    except AttributeError as exp:
        raise AttributeError
        logging.error("Attribute missing", exc_info=True)
    except Exception as exp:
        logging.error("Error occured while calculating the total cost", exc_info=True)
    return order_cost

#Calculates the total units to be added in the basket after applying the offers
def calculate_total_product_units_offer(requested_product_unit, catalog_id):
    number_of_products=0
    try:
        logging.info(requested_product_unit)
        if requested_product_unit != None and catalog_id != None:
            offer = get_offer_for_catalog(catalog_id)
            number_of_products = requested_product_unit + (requested_product_unit*offer.discount_fractional_value_on_unit)
    except AttributeError as exp:
        raise AttributeError
        logging.error("Attribute missing", exc_info=True)
    except Exception as exp:
        logging.error("Error occured while calculating the total cost", exc_info=True)
    return number_of_products

def save_changes(data):
    db.session.add(data)
    db.session.commit()

def get_orders():
    return Order.query.all()

def get_a_order(order_id):
    return Order.query.filter_by(orderid=order_id).first()

def get_all_product_catalog():
    return ProductCatalog.query.all()

def get_product_catalog_for_id(catalog_id):
    return ProductCatalog.query.filter_by(catalog_id=catalog_id).first()

def get_offer_for_catalog(catalog_id):
    return Offer.query.filter_by(catalog_id=catalog_id).first()
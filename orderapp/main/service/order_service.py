import uuid, datetime
import logging

from orderapp.main.model.order_dto import OrderDto
from orderapp.main.model.order_model import Order
from orderapp.main.model.product_model import Product

from orderapp.db import db

from sqlalchemy.exc import SQLAlchemyError

#Logging configurations
logging.basicConfig(level=logging.DEBUG)

product = OrderDto.product

#Product cost 
productcost = {'Apples': 1, 'Oranges':0.7}

def save_order(order_request):
    order = lambda: None
    try:
        if order_request != None:
            order_id = str(uuid.uuid4())
            products = []
            product_request = order_request['products']
            
            if  product_request != None:
                for product in product_request:
                    product = Product(
                        producttype=product['producttype'],
                        units=product['units'],
                        order_id=order_id
                    )
                    products.append(product)

            order = Order(
                username=order_request['username'],
                orderid=order_id,
                orderdate=datetime.datetime.utcnow(),
                totalordercost=calculate_total_order_cost(order_request['products']),
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
                product_type = product['producttype']
                number_of_products = product['units']
                logging.info(product['units'])

                if (product_type=='Apples'):
                    order_cost = order_cost + productcost['Apples']*number_of_products
                elif (product_type=='Oranges'):
                    order_cost = order_cost + productcost['Oranges']*number_of_products
    except KeyError as exp:
        raise KeyError
        logging.error("Key missing", exc_info=True)
    except Exception as exp:
        logging.error("Error occured while calculating the total cost", exc_info=True)
    return order_cost

def save_changes(data):
    db.session.add(data)
    db.session.commit()

def get_orders():
    return Order.query.all()

def get_a_order(order_id):
    return Order.query.filter_by(orderid=order_id).first()
import uuid, datetime
import logging

from ..model.order_dto import OrderDto
from ..model.order_model import Order
from ..model.product_model import Product

#Logging configurations
logging.basicConfig(level=logging.DEBUG)

product = OrderDto.product

#Product cose 
productcost = {'Apples': 1, 'Oranges':0.7}

orders = {}


def save_order(order_request):
    order = lambda: None
    try:
        if order_request != None:
            orderid = uuid.uuid4()
            products = []
            if order_request['products'] != None:
                for product in order_request['products']:
                    product = Product(
                        producttype=product['producttype'],
                        units=product['units']
                    )
                    products.append(product)

            order = Order(
                username=order_request['username'],
                orderid=orderid,
                orderdate=datetime.datetime.utcnow(),
                totalordercost=calculate_total_order_cost(order_request['products']),
                products=products
            )
    
            orders[orderid]=order
        else:
            order = None
    except KeyError as exp:
        raise KeyError
        logging.error("Key missing", exc_info=True)
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
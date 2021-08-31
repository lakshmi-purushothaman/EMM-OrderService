"""Initialization script to load test data into the DB."""
from orderapp.main.model.order_model import Order 
from orderapp.main.model.product_model import Product
from orderapp.main.model.offer_model import Offer
from orderapp.main.model.product_catalog_model import ProductCatalog

from orderapp.db import db
from orderapp.main import app

import datetime

def init_db(app):
    """Init the DB with some setup data."""
    with app.app_context():
        db.drop_all()
        db.create_all()
        create_order_data()
        create_catalog_data()
        create_offer_data()
        
def create_order_data():
    orders = [
            Order(username = "Test User1",
                orderid = "Test ID",
                orderdate= datetime.datetime.utcnow(),
                products= [ Product(producttype="Apples", units= 11, discountedunits=22,order_id="Test ID",catalog_id=1),
                            Product(producttype="Oranges", units= 10, discountedunits=15,order_id="Test ID",catalog_id=2)
                ],
                totalordercost = 18)
            ]
    for order in orders:
        save_session(order)

def create_offer_data():
    offers = [
            Offer(description="Buy 1 get 1 free on Apples",discount_fractional_value_on_unit=1,offer_id=1,catalog_id=1),
            Offer(description="3 for 2 on Oranges",discount_fractional_value_on_unit=0.5,offer_id=2,catalog_id=2)
    ]
    for offer in offers:
        save_session(offer)

def create_catalog_data():
    catalogs = [
            ProductCatalog(producttype="Apples",cost=0.60,offer_id=1,catalog_id=1),
            ProductCatalog(producttype="Buy 1 get 1 free on Apples",cost=0.25,offer_id=2,catalog_id=2)
    ]
    for catalog in catalogs:
        save_session(catalog)

def save_session(data):
    db.session.add(data)
    db.session.commit()
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
        #create_catalog_data()
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
    applecatalog = [
            ProductCatalog(producttype="Apples",cost=1.5,offer_id=1,catalogid=1)
    ]
    orangecatalog = [
            ProductCatalog(producttype="Oranges",cost=2,offer_id=2,catalogid=2)
    ]
    offers = [
            Offer(description="Buy 1 get 1 free on Apples",discountfractiononunits=1,offerid=1,catalogs=applecatalog),
            Offer(description="3 for 2 on Oranges",  discountfractiononunits=0.5,offerid=2,catalogs=orangecatalog)
    ]
    for offer in offers:
        save_session(offer)

def save_session(data):
    db.session.add(data)
    db.session.commit()
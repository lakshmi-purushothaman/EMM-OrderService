"""Initialization script to load test data into the DB."""
from orderapp.main.model.order_model import Order 
from orderapp.main.model.product_model import Product

from orderapp.db import db
from orderapp.main import app

import datetime

def init_db(app):
    """Init the DB with some setup data."""
    with app.app_context():
        db.drop_all()
        db.create_all()
        orders = [
            Order(username = "Test User1",
                orderid = "Test ID",
                orderdate= datetime.datetime.utcnow(),
                products= [ Product(producttype="Apples", units= 11, order_id="Test ID"),
                            Product(producttype="Oranges", units= 10, order_id="Test ID")
                ],
                totalordercost = 18)
            ]
        for order in orders:
            db.session.add(order)
            db.session.commit()
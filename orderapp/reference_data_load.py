"""Initialization script to load test data into the DB."""
from orderapp.main.model.offer_model import Offer
from orderapp.main.model.product_catalog_model import ProductCatalog

from orderapp.db import db

import datetime
        
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
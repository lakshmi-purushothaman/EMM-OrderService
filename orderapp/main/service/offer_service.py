from orderapp.main.model.offer_model import Offer

def get_offers():
    return Offer.query.all()
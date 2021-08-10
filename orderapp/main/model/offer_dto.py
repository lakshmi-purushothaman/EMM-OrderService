from flask_restplus import Namespace,fields

class OfferDto:
    offerapi = Namespace("Offer", description="Product Offers")

    offer = offerapi.model('Offer',{
        'offerID': fields.Integer(required=True, description='ID of the offer'),
        'offerDescription': fields.String(required=True, description ='Offer description'),
        'discountFraction': fields.Float(required=True, description='Fractional representation of the discount')
    })
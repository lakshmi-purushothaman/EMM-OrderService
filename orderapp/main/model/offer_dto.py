from flask_restplus import Namespace,fields

class OfferDto:
    offerapi = Namespace("Offer", description="Product Offers")

    catalog = offerapi.model('ProductCatalog',{
        'catalogid':fields.Integer(required=True, description='Catalog ID'),
        'producttype':fields.String(required=True, description='The product type that is available to place a order'),
        'cost':fields.Float(required=True, description='Unit price of the product')
    })

    offer = offerapi.model('Offer',{
        'offerid': fields.Integer(required=True, description='ID of the offer'),
        'description': fields.String(required=True, description ='Offer description'),
        'discountfractiononunits': fields.Float(required=True, description='Fractional representation of the discount'),
        'catalogs': fields.List(fields.Nested(catalog, required=True))
    })
from flask_restplus import Namespace, fields

class OrderDto:
    
    api = Namespace('fruitorders', description='Fruit order operations')
    
    ##Model
    product = api.model('Product', {
        'producttype': fields.String(required=True, description='The product type that is available to place a order', enum=['Apples','Oranges'], default='Apples'),
        'units': fields.Integer(required=True, description='The amount of units of the product requested by the client', default=1)
    })
    
    orderRequest = api.model('OrderRequest', {
        'username': fields.String(required=True, default='Adam'),
        'products':fields.List(fields.Nested(product, required= True))
    })

    productResponse = api.model('ProductResponse', {
        'producttype': fields.String(required=True, description='The product type that is available to place a order', enum=['Apples','Oranges'], default='Apples'),
        'units': fields.Integer(required=True, description='The amount of units of the product requested by the client', default=1),
        'discountedunits': fields.Integer(required=True, description='The amount of units after applying the offer', default=0)
    })
    orderResponse = api.model('OrderResponse', {
        'username': fields.String(required=True, default='Adam'),
        'orderid': fields.String(required=True),
        'orderdate': fields.DateTime(required=True),
        'products':fields.List(fields.Nested(productResponse, required= True)),
        'totalordercost': fields.Float(required=True)
    })
from .product_model import Product

class Order(Product):

    def __init__(self,username,orderid,orderdate,totalordercost,products):
        self.username = username
        self.orderid = orderid
        self.orderdate = orderdate
        self.totalordercost = totalordercost
        self.products = products

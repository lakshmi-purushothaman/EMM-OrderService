from orderapp.main import db

from .product_model import Product

class Order(db.Model):
    __tablename__='order'
    
    id=db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    orderdate = db.Column(db.DateTime, nullable=False)
    totalordercost=db.Column(db.Integer, nullable=False)
    orderid = db.Column(db.String, nullable=False, unique=True)
    products = db.relationship("Product",lazy="dynamic",primaryjoin="Order.id == Product.order_id")


    def __init__(self,username,orderid,orderdate,totalordercost,products):
        self.username = username
        self.orderid = orderid
        self.orderdate = orderdate
        self.totalordercost = totalordercost
        self.products = products

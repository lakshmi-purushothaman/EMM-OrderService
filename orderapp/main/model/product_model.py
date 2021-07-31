from orderapp.main import db

class Product(db.Model):
    __tablename__='product'

    id=db.Column(db.Integer, primary_key=True)
    producttype = db.Column(db.String(80), nullable=False)
    units = db.Column(db.Integer, nullable=False)
    order_id = db.Column(db.String,db.ForeignKey('order.id'),nullable=False)

    order = db.relationship("Order",)

    def __init__(self,producttype,units,order_id):
        self.producttype=producttype
        self.units=units
        self.order_id=order_id
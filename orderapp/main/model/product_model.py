from orderapp.main import db

class Product(db.Model):
    __tablename__='product'

    id=db.Column(db.Integer, primary_key=True)
    producttype = db.Column(db.String(80), nullable=False)
    units = db.Column(db.Integer, nullable=False)
    discountedunits = db.Column(db.Integer, nullable=False)
    order_id = db.Column(db.String,db.ForeignKey('order.id'),nullable=False)
    catalog_id = db.Column(db.Integer, db.ForeignKey('product_catalog.catalog_id'),nullable=False)

    def __init__(self,producttype,units,discountedunits,order_id,catalog_id):
        self.producttype=producttype
        self.units=units
        self.discountedunits=discountedunits
        self.order_id=order_id
        self.catalog_id=catalog_id
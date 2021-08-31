from orderapp.main import db

class ProductCatalog(db.Model):
    __tablename__='product_catalog'

    id=db.Column(db.Integer, primary_key=True)
    catalogid = db.Column(db.Integer, nullable=False)
    producttype = db.Column(db.String(80), nullable=False)
    cost = db.Column(db.Float, nullable=False)
    offer_id = db.Column(db.String,db.ForeignKey('offer.id'),nullable=False)

    def __init__(self,catalogid,producttype,cost,offer_id):
        self.catalogid=catalogid
        self.producttype=producttype
        self.cost=cost
        self.offer_id=offer_id

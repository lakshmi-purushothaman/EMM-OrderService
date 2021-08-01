from orderapp.main import db

class ProductCatalog(db.Model):
    __tablename__='product_catalog'

    id=db.Column(db.Integer, primary_key=True)
    catalog_id = db.Column(db.Integer, nullable=False)
    producttype = db.Column(db.String(80), nullable=False)
    cost = db.Column(db.Float, nullable=False)
    offer_id = db.Column(db.String,db.ForeignKey('offer.offer_id'),nullable=False)

    def __init__(self,catalog_id,producttype,cost,offer_id):
        self.catalog_id=catalog_id
        self.producttype=producttype
        self.cost=cost
        self.offer_id=offer_id
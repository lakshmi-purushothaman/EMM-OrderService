from orderapp.main import db

class Offer(db.Model):
    __tablename__='offer'

    id=db.Column(db.Integer, primary_key=True)
    offer_id = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    discount_fractional_value_on_unit = db.Column(db.Float, nullable=False)
    catalog_id = db.Column(db.Integer, db.ForeignKey('product_catalog.catalog_id'),nullable=False)

    def __init__(self,offer_id,description,discount_fractional_value_on_unit,catalog_id):
        self.offer_id=offer_id
        self.description=description
        self.discount_fractional_value_on_unit=discount_fractional_value_on_unit
        self.catalog_id=catalog_id
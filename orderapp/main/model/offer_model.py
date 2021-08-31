from orderapp.main import db

class Offer(db.Model):
    __tablename__='offer'

    id=db.Column(db.Integer, primary_key=True)
    offerid = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    discountfractiononunits = db.Column(db.Float, nullable=False)
    catalogs = db.relationship("ProductCatalog",lazy="dynamic",primaryjoin="Offer.id == ProductCatalog.offer_id")


    def __init__(self,offerid,description,discountfractiononunits,catalogs):
        self.offerid=offerid
        self.description=description
        self.discountfractiononunits=discountfractiononunits
        self.catalogs=catalogs
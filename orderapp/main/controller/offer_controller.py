from flask_restplus import Resource

from orderapp.main.model.offer_dto import OfferDto
from orderapp.main.service.offer_service import get_offers

offerapi=OfferDto.offerapi

offer_response = OfferDto.offer

@offerapi.route('/')
class Offer_List(Resource):
    @offerapi.marshal_with(offer_response, envelope="data", code=200)
    def get(self):
        return get_offers()
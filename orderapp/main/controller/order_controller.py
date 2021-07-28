from flask import request

from flask_restplus import Resource

from ..model.order_dto import OrderDto

from ..service.order_service import save_order

api = OrderDto.api
order_request = OrderDto.orderRequest
order_response = OrderDto.orderResponse


@api.route('/')
class Order(Resource):
    @api.expect(order_request, validate=True)
    @api.doc("This endpoint should be consumed to place a fruit order")
    @api.marshal_with(order_response, envelope="data", code=200)
    def post(self):
        return save_order(request.json)
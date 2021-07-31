from flask import request

from flask_restplus import Resource

from ..model.order_dto import OrderDto

from ..service.order_service import save_order, get_orders, get_a_order

api = OrderDto.api
order_request = OrderDto.orderRequest
order_response = OrderDto.orderResponse


@api.route('/')
class Order_List(Resource):
    @api.expect(order_request, validate=True)
    @api.doc("This endpoint should be consumed to place a fruit order")
    @api.marshal_with(order_response, envelope="data", code=200)
    def post(self):
        return save_order(request.json)

    @api.marshal_with(order_response, envelope="data", code=200)
    def get(self):
        return get_orders()

@api.route('/<order_id>')
@api.param('order_id', "Order Identifier")
@api.response(404, "Order not found")
class Order(Resource):
    @api.doc("Order ID")
    @api.marshal_with(order_response, envelope="data", code=200)
    def get(self,order_id):
        order = get_a_order(order_id)
        if not order:
            api.abort(404)
        else:
            return order
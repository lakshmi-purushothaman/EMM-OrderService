import pytest

from ..main.model.order_dto import OrderDto
from ..main.service.order_service import save_order

order_request = OrderDto.orderRequest

def test_save_order():
    order_request = { "ordername": "string",
                        "products": {
                            "producttype": "Apples",
                            "units":11
                        }
                    }
    order = save_order(order_request)
    assert order is not None

def test_save_order_without_request():
    order_request = None
    order = save_order(order_request)
    assert order is None

def test_save_order_without_products():
    with pytest.raises(KeyError) as exc_info:
        order_request = { "ordername": "string"
                        }
        order = save_order(order_request)
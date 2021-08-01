import pytest
import logging

from orderapp.main.model.order_dto import OrderDto
from orderapp.main.service.order_service import save_order, get_orders, get_a_order
from orderapp.main.model.order_model import Order

from orderapp.main import app

from orderapp.test.test_data_load import init_db

order_request = OrderDto.orderRequest

#Logging configurations
logging.basicConfig(level=logging.DEBUG)

@pytest.fixture
def app_inst():
    #Pytest fixture that returns an instance of application.
    app.debug = True
    # Load test DB objects
    init_db(app)
    return app

def test_save_order():
    order_request = { "username": "Test User Post",
                        "products": [
                            {
                                "producttype": "Apples",
                                "units":11
                            }
                        ]
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

def test_get_all_orders_200(app_inst):
    client = app_inst.test_client()
    response = client.get("/order/")
    assert response.status_code == 200

def test_get_all_orders_data(app_inst):
    client = app_inst.test_client()
    response = client.get("/order/")
    assert b'"username": "Test User1"' in response.data

def test_get_a_order_404(app_inst):
    client = app_inst.test_client()
    response = client.get("/order/1")
    assert response.status_code == 404

def test_get_a_order_200(app_inst):
    client = app_inst.test_client()
    response = client.get("/order/Test ID")
    assert response.status_code == 200

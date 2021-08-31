import pytest
import logging, json

from orderapp.main.model.order_dto import OrderDto
from orderapp.main.service.order_service import save_order, get_orders, get_a_order, calculate_total_product_units_offer, calculate_total_order_cost
from orderapp.main.model.order_model import Order
from orderapp.main.model.product_model import Product

from orderapp.main import app

from orderapp.test.test_data_load import init_db

from mock_alchemy.mocking import UnifiedAlchemyMagicMock

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

def test_save_order_200(app_inst):
    order_request = { "username": "Test User Data Check",
                      "products": [
                            {
                            "producttype": "Apples",
                            "units": 10
                            }
                        ]
                    }

    client = app_inst.test_client()
    response = client.post("/order/fruitorders/", data=json.dumps(order_request), headers={"Content-Type": "application/json"})
    assert response.status_code == 200

def test_save_order_check_for_data(app_inst):
    order_request = { "username": "Test User Data Check",
                      "products": [
                            {
                            "producttype": "Apples",
                            "units": 5
                            }
                        ]
                    }

    client = app_inst.test_client()
    response = client.post("/order/fruitorders/", data=json.dumps(order_request), headers={"Content-Type": "application/json"})
    assert b'"username": "Test User Data Check"' in response.data
    assert b'"discountedunits": 10' in response.data
    
def test_get_all_orders_200(app_inst):
    client = app_inst.test_client()
    response = client.get("/order/fruitorders/")
    assert response.status_code == 200

def test_get_all_orders_data(app_inst):
    client = app_inst.test_client()
    response = client.get("/order/fruitorders/")
    assert b'"username": "Test User1"' in response.data

def test_get_a_order_404(app_inst):
    client = app_inst.test_client()
    response = client.get("/order/fruitorders/1")
    assert response.status_code == 404

def test_get_a_order_200(app_inst):
    client = app_inst.test_client()
    response = client.get("/order/fruitorders/Test ID")
    assert response.status_code == 200
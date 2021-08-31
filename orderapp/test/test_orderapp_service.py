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

def test_save_order_without_products_raises_exception():
    with pytest.raises(Exception) as exc_info:
        order_request = { "username": "Test User Post"}
        order = save_order(order_request)

def test_save_order_raises_key_error():
    with pytest.raises(KeyError) as exc_info:
        order_request = { "ordername": "string"
                        }
        order = save_order(order_request)

def test_calculate_total_order_cost():
    with app.app_context():
        products =  [Product(producttype='Apples',
                                units=10,
                                discountedunits=0,
                                order_id="Test ID",
                                catalog_id=1
                                )]
        order_cost = calculate_total_order_cost(products)
        assert order_cost == 6

def test_calculate_total_order_cost_raises_attribute_error():
    with app.app_context():
        with pytest.raises(AttributeError) as exc_info:
            products =  [Product(producttype='Apples',
                                    units=10,
                                    discountedunits=0,
                                    order_id="Test ID",
                                    catalog_id=12
                                    )]
            order_cost = calculate_total_order_cost(products)

def test_calculate_total_product_units_offer():
    with app.app_context():
        number_of_discounted_products = calculate_total_product_units_offer(10, 1)
        assert number_of_discounted_products == 20

def test_calculate_total_product_units_offer_raises_attribute_error():
    with app.app_context():
        with pytest.raises(AttributeError) as exc_info:
            number_of_discounted_products = calculate_total_product_units_offer(10, 100)
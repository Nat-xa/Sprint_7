import allure
import pytest

from data import CreateOrder
from helper import Helper
from interface_api import InterfaceApi


class TestCreateOrderEndpoint:
    @pytest.mark.parametrize(CreateOrder.param, CreateOrder.value)
    @allure.title('Проверка создания заказа')
    def test_create_order_success(self, first_name, last_name, address, metro_station, phone, rent_time,
                                  delivery_date, comment, color):
        body_request = Helper.create_body_for_create_order(first_name, last_name, address, metro_station,
                                                           phone, rent_time, delivery_date, comment, color)
        create_response = InterfaceApi.create_order_endpoint(body_request)
        order_track = Helper.generate_payload_to_get_track(create_response.json()['track'])
        InterfaceApi.delete_order_to_track(order_track)
        assert create_response.status_code == 201 and 'track' in create_response.text

import allure

from data import OrderToTrack, CreateOrder
from helper import Helper
from interface_api import InterfaceApi


class TestGetOrderToTrackEndpoint:

    @allure.title('Проверка успешного получения заказа по его номеру')
    def test_get_order_to_track_success(self):
        order_track = InterfaceApi.create_order_endpoint(CreateOrder.CREATE_ORDER_BODY).json()['track']
        response = InterfaceApi.get_order_to_track(Helper.generate_payload_to_get_track(order_track))
        assert response.status_code == 200 and response.json()['order']['track'] == order_track

    @allure.title('Проверка получения заказа с несуществующим номером (треком)')
    def test_get_order_to_track_false_order(self):
        response = InterfaceApi.get_order_to_track(OrderToTrack.PAYLOAD_FALSE_ORDER)
        assert (response.status_code == 404 and response.json()['message'] == OrderToTrack.
                TEXT_ERROR_ORDER_TO_TRACK_404)

    @allure.title('Проверка получения заказа без номера (трека)')
    def test_get_order_to_track_without_track_order(self):
        response = InterfaceApi.get_order_to_track(OrderToTrack.PAYLOAD_WITHOUT_TRACK_ORDER)
        assert (response.status_code == 400 and response.json()['message'] == OrderToTrack.
                TEXT_ERROR_ORDER_TO_TRACK_400)

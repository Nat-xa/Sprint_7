import allure

from interface_api import InterfaceApi


class TestGetListOrderEndpoint:

    @allure.title('Проверка получения списка заказов без ID курьера')
    def test_get_list_order_success(self):
        response = InterfaceApi.get_list_order_endpoint()
        assert response.status_code == 200 and len(response.json()) > 0

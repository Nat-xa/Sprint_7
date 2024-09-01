import allure

from data import DeleteCourier
from helper import Helper
from interface_api import InterfaceApi


class TestDeleteCourierEndpoint:
    @allure.title('Проверка удаления созданного курьера')
    def test_delete_courier_success(self):
        courier_body = Helper.create_new_courier()
        InterfaceApi.create_courier_endpoint(courier_body)
        body_login = Helper.modify_courier_body_to_body_login(courier_body)
        login = InterfaceApi.login_endpoint(body_login)
        courier_id = login.json()['id']
        delete_response = InterfaceApi.delete_courier_to_id(courier_id)
        assert (delete_response.status_code == 200 and delete_response.json() == DeleteCourier.
                SUCCESS_DELETE_REQUESTS)

    @allure.title('Проверка удаления курьера без ID')
    def test_delete_courier_without_id(self):
        delete_response = InterfaceApi.delete_courier_to_id(DeleteCourier.ID_NUMBER_EMPTY)
        assert (delete_response.status_code == 400 and delete_response.json()['message'] == DeleteCourier.
                TEXT_ERROR_DELETE_COURIER_400)

    @allure.title('Проверка удаления курьера с несуществующим ID')
    def test_delete_courier_false_id(self):
        delete_response = InterfaceApi.delete_courier_to_id(DeleteCourier.ID_NUMBER_FALSE)
        assert (delete_response.status_code == 404 and delete_response.json()['message'] == DeleteCourier.
                TEXT_ERROR_DELETE_COURIER_404)

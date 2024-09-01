import allure

from data import CreateCourier
from helper import Helper
from interface_api import InterfaceApi


class TestCreateCourierEndpoint:
    @allure.title('Проверка успешного создания курьера')
    @allure.description('Проверка успешного создания курьера с уникальными рандомными данными '
                        '(с удалением созданных тестовых данных)')
    def test_create_new_courier_success(self):
        body = Helper.create_new_courier()
        create_response = InterfaceApi.create_courier_endpoint(body)
        courier_id = InterfaceApi.login_endpoint(Helper.modify_courier_body_to_body_login(body)).json()['id']
        delete_courier = InterfaceApi.delete_courier_to_id(courier_id)
        assert (create_response.status_code == 201 and create_response.json() ==
                CreateCourier.CREATE_SUCCESS_RESPONSE) and delete_courier.status_code == 200

    @allure.title('Проверка создания курьера с повторяющимся логином')
    def test_create_two_same_courier(self):
        body = Helper.create_new_courier()
        InterfaceApi.create_courier_endpoint(body)
        create_response = InterfaceApi.create_courier_endpoint(body)
        assert (create_response.status_code == 409 and create_response.json()['message'] ==
                CreateCourier.TEXT_ERROR_CREATE_409)

    @allure.title('Проверка создания курьера без пароля')
    def test_create_new_courier_without_pass(self):
        create_response = InterfaceApi.create_courier_endpoint(Helper.
                                                               modify_create_body_request_without_password())
        assert (create_response.status_code == 400 and create_response.json()['message'] ==
                CreateCourier.TEXT_ERROR_CREATE_400)

    @allure.title('Проверка создания курьера без логина')
    def test_create_new_courier_without_login(self):
        create_response = InterfaceApi.create_courier_endpoint(Helper.modify_create_body_request_without_login())
        assert (create_response.status_code == 400 and create_response.json()['message'] ==
                CreateCourier.TEXT_ERROR_CREATE_400)

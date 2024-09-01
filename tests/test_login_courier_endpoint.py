import allure

from data import Login
from interface_api import InterfaceApi


class TestLoginCourierEndpoint:

    @allure.title('Проверка успешной авторизации курьера')
    def test_login_courier_success(self):
        login_response = InterfaceApi.login_endpoint(Login.LOGIN_COURIER_BODY_SUCCESS)
        assert login_response.status_code == 200 and login_response.json()['id'] == Login.COURIER_SUCCESS_ID

    @allure.title('Проверка авторизации курьера с несуществующей парой логин-пароль')
    def test_login_non_existent_courier(self):
        login_response = InterfaceApi.login_endpoint(Login.LOGIN_COURIER_NON_EXISTENT_BODY)
        assert login_response.status_code == 404 and login_response.json()['message'] == Login.TEXT_ERROR_LOGIN_404

    @allure.title('Проверка авторизации курьера без пароля')
    def test_login_without_password(self):
        login_response = InterfaceApi.login_endpoint(Login.LOGIN_COURIER_BODY_WITHOUT_PASS)
        assert login_response.status_code == 400 and login_response.json()['message'] == Login.TEXT_ERROR_LOGIN_400

    @allure.title('Проверка авторизации курьера с неверным паролем')
    def test_login_with_false_password(self):
        login_response = InterfaceApi.login_endpoint(Login.LOGIN_COURIER_BODY_FALSE_PASS)
        assert login_response.status_code == 404 and login_response.json()['message'] == Login.TEXT_ERROR_LOGIN_404

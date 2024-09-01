class Login:
    # Данные для успешной авторизации курьера
    LOGIN_COURIER_BODY_SUCCESS = {
        "login": "Ann",
        "password": "1234"
    }
    # Данные для авторизации с несуществующим логином
    LOGIN_COURIER_NON_EXISTENT_BODY = {
        "login": "RHS5",
        "password": "1234"
    }
    # Данные для авторизации без пароля
    LOGIN_COURIER_BODY_WITHOUT_PASS = {
        "login": "Ann",
        "password": ""
    }
    # Данные для авторизации с неверным паролем
    LOGIN_COURIER_BODY_FALSE_PASS = {
        "login": "Ann",
        "password": "987"
    }
    # Текст ошибки при авторизации с несуществующей парой логин-пароль
    TEXT_ERROR_LOGIN_404 = "Учетная запись не найдена"
    # Текст ошибки при авторизации без логина или пароля
    TEXT_ERROR_LOGIN_400 = "Недостаточно данных для входа"
    # Id сущесвующего курьера
    COURIER_SUCCESS_ID = 373447


class CreateCourier:

    # Тело ответа при успешном создании курьера
    CREATE_SUCCESS_RESPONSE = {"ok": True}
    # Текст ошибки при создании курьера с повторяющимся логином
    TEXT_ERROR_CREATE_409 = "Этот логин уже используется"
    # Текст ошибки при создании курьера без логина или пароля
    TEXT_ERROR_CREATE_400 = "Недостаточно данных для создания учетной записи"


class CreateOrder:

    param = 'first_name, last_name, address, metro_station, phone, rent_time, delivery_date, comment, color'
    value = [
        ['Василиса', 'Иванова', 'Москва, д.7', '8', '+79154445566', '5', '2024-09-01', '', ["BLACK"]],
        ['Вася', 'Петров', 'Москва, д.111', '3', '+79158974542', '2', '2024-09-11', '', [""]],
        ['Vova', 'Kot', 'Москва, ул. Ленинградская, д.1', '8', '+79150000000', '1', '2024-09-05', '', ["GREY"]],
        ['Галина', 'Сидорова', 'Москва,ул.Победы, д.9', '1', '+79154445566', '4', '2024-09-01', '', ["BLACK", "GREY"]],
    ]
    # Данные для успешного создания заказа
    CREATE_ORDER_BODY = {
        "firstName": "Олег",
        "lastName": "Смирнов",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "тестовый комментарий",
        "color": [
            "BLACK"
        ]
    }


class OrderToTrack:

    # Параметр для получения заказа по треку с несуществующим номером трека
    PAYLOAD_FALSE_ORDER = {"t": "123456"}
    # Текст ошибки при получении заказа по треку без номера трека
    TEXT_ERROR_ORDER_TO_TRACK_404 = "Заказ не найден"
    # Параметр для получения заказа с пустым номером трека
    PAYLOAD_WITHOUT_TRACK_ORDER = {"t": ""}
    # Текст ошибки при получении заказа по треку с пустынм номером трека
    TEXT_ERROR_ORDER_TO_TRACK_400 = "Недостаточно данных для поиска"


class DeleteCourier:

    # Пустой Id курьера для удаления
    ID_NUMBER_EMPTY = " "
    # Несуществующий Id курьера для удаления
    ID_NUMBER_FALSE = "0"
    # Текст ошибки при удалении курьера с несуществующим Id
    TEXT_ERROR_DELETE_COURIER_404 = "Курьера с таким id нет"
    # Текст ошибки при удалении курьера без Id
    TEXT_ERROR_DELETE_COURIER_400 = "Недостаточно данных для удаления курьера"
    # Тело ответа при успешном удалении курьера
    SUCCESS_DELETE_REQUESTS = {"ok": True}

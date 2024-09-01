import random
import string


class Helper:

    @staticmethod
    def create_new_courier():
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        body = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return body

    @staticmethod
    def modify_create_body_request(key, value):
        body = Helper.create_new_courier().copy()
        body[key] = value

        return body

    @staticmethod
    def modify_create_body_request_without_password():
        return Helper.modify_create_body_request('password', '')

    @staticmethod
    def modify_create_body_request_without_login():
        return Helper.modify_create_body_request('login', '')

    @staticmethod
    def create_body_for_create_order(first_name, last_name, address, metro_station, phone, rent_time,
                                     delivery_date, comment, color):
        body = {
            "firstName": first_name,
            "lastName": last_name,
            "address": address,
            "metroStation": metro_station,
            "phone": phone,
            "rentTime": rent_time,
            "deliveryDate": delivery_date,
            "comment": comment,
            "color": [color]
        }
        return body

    @staticmethod
    def generate_payload_to_get_track(order_track):
        return {"t": order_track}

    @staticmethod
    def modify_courier_body_to_body_login(courier_body):
        login = courier_body['login']
        password = courier_body['password']
        body_new = {
            "login": login,
            "password": password
        }
        return body_new

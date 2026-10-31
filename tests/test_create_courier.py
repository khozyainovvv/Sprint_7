import pytest
import allure
import requests
from conftest import BASE_URL, generate_random_string


@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self, courier_data):
        response = requests.post(f"{BASE_URL}/api/v1/courier", data=courier_data)
        assert response.status_code == 201, "Неверный код ответа"
        assert response.json() == {"ok": True}, "Неверное тело ответа"

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier(self, created_courier):
        response = requests.post(f"{BASE_URL}/api/v1/courier", data=created_courier)
        assert response.status_code == 409, "Неверный код ответа"
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой.", \
            "Неверное сообщение об ошибке"

    @allure.title("Создание курьера без логина")
    def test_create_courier_without_login(self, courier_data):
        courier_data.pop("login")
        response = requests.post(f"{BASE_URL}/api/v1/courier", data=courier_data)
        assert response.status_code == 400, "Неверный код ответа"
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи", \
            "Неверное сообщение об ошибке"

    @allure.title("Создание курьера без пароля")
    def test_create_courier_without_password(self, courier_data):
        courier_data.pop("password")
        response = requests.post(f"{BASE_URL}/api/v1/courier", data=courier_data)
        assert response.status_code == 400, "Неверный код ответа"
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи", \
            "Неверное сообщение об ошибке"
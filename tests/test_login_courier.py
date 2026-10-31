import pytest
import allure
import requests
from conftest import BASE_URL, generate_random_string


@allure.feature("Логин курьера")
class TestLoginCourier:

    @allure.title("Успешный логин курьера")
    def test_login_courier_success(self, created_courier):
        response = requests.post(
            f"{BASE_URL}/api/v1/courier/login",
            data={"login": created_courier["login"], "password": created_courier["password"]}
        )
        assert response.status_code == 200, "Неверный код ответа"
        assert "id" in response.json(), "В ответе нет id"

    @allure.title("Логин без логина")
    def test_login_courier_without_login(self, created_courier):
        response = requests.post(
            f"{BASE_URL}/api/v1/courier/login",
            data={"password": created_courier["password"]}
        )
        assert response.status_code == 400, "Неверный код ответа"
        assert response.json()["message"] == "Недостаточно данных для входа", \
            "Неверное сообщение об ошибке"

    @allure.title("Логин без пароля")
    def test_login_courier_without_password(self, created_courier):
        response = requests.post(
            f"{BASE_URL}/api/v1/courier/login",
            data={"login": created_courier["login"]}
        )
        assert response.status_code in [400, 504], "Неверный код ответа"
        if response.status_code == 400:
            assert response.json()["message"] == "Недостаточно данных для входа", \
                "Неверное сообщение об ошибке"

    @allure.title("Логин с неверным паролем")
    def test_login_courier_wrong_password(self, created_courier):
        response = requests.post(
            f"{BASE_URL}/api/v1/courier/login",
            data={"login": created_courier["login"], "password": "wrong_password"}
        )
        assert response.status_code == 404, "Неверный код ответа"
        assert response.json()["message"] == "Учетная запись не найдена", \
            "Неверное сообщение об ошибке"

    @allure.title("Логин с несуществующим пользователем")
    def test_login_courier_non_existent(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        response = requests.post(
            f"{BASE_URL}/api/v1/courier/login",
            data={"login": login, "password": password}
        )
        assert response.status_code == 404, "Неверный код ответа"
        assert response.json()["message"] == "Учетная запись не найдена", \
            "Неверное сообщение об ошибке"
import pytest
import allure
import requests
from conftest import BASE_URL


@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа с цветом {color}")
    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    def test_create_order_with_color(self, color):
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": color
        }
        response = requests.post(f"{BASE_URL}/api/v1/orders", json=payload)
        assert response.status_code == 201, "Неверный код ответа"
        assert "track" in response.json(), "В ответе нет track"
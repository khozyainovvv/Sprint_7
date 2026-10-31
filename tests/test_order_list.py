import pytest
import allure
import requests
from conftest import BASE_URL


@allure.feature("Список заказов")
class TestOrderList:

    @allure.title("Получение списка заказов")
    def test_get_order_list(self):
        response = requests.get(f"{BASE_URL}/api/v1/orders")
        assert response.status_code == 200, "Неверный код ответа"
        assert "orders" in response.json(), "В ответе нет списка заказов"
        assert isinstance(response.json()["orders"], list), "orders — не список"
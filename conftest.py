import pytest
import requests
import random
import string


BASE_URL = "https://qa-scooter.education-services.ru"


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


@pytest.fixture
def courier_data():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    return {"login": login, "password": password, "firstName": first_name}


@pytest.fixture
def created_courier(courier_data):
    response = requests.post(f"{BASE_URL}/api/v1/courier", data=courier_data)
    courier_id = None
    if response.status_code == 201:
        login_response = requests.post(
            f"{BASE_URL}/api/v1/courier/login",
            data={"login": courier_data["login"], "password": courier_data["password"]}
        )
        if login_response.status_code == 200:
            courier_id = login_response.json().get("id")
    
    yield courier_data
    
    if courier_id:
        requests.delete(f"{BASE_URL}/api/v1/courier/{courier_id}")
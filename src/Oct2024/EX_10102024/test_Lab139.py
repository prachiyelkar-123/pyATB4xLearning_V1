# PUT - Request
# URL
# Path - Booking ID
# Token - Auth
# Payload
# Headers
from tokenize import cookie_re

import pytest
import allure
import requests

@allure.title("TC#1 - create token positive")
@allure.description("Verify to create token")
@pytest.mark.CRUD
def test_create_token():
    URL = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type":"application/json"}
    payload = {
        "username" : "admin",
        "password" : "password123"
}

    response = requests.post(url=URL, headers=headers, json=payload)
    token = response.json()["token"]
    print(token)
    return token

#create booking
@allure.title("TC#1 - create booking positive")
@allure.description("Verify create booking ID")
@pytest.mark.CRUD

def test_create_booking_ID():
    base_URL = "https://restful-booker.herokuapp.com"
    base_path =  "/booking"
    URL = base_URL + base_path
    headers = {"Content-Type" : "application/json", "Accept" : "application/json"}
    payload ={
        "firstname" : "Alka",
        "lastname" : "Yelkar",
        "totalprice" : 2000,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2024-01-25",
            "checkout" : "2024-01-29"
        },
        "additionalneeds" : "breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=payload)
    assert response.status_code == 200
    data = response.json()
    booking_id = data["bookingid"]
    return booking_id

#Put request

def test_post_request():
    base_URL = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(test_create_booking_ID())
    PUT_URL = base_URL + base_path
    cookie = "token=" + test_create_token()
    headers = {"Content-Type" : "application/json", "cookie" : cookie}
    payload = {
        "firstname": "Alka",
        "lastname": "Yelkar",
        "totalprice": 2000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-25",
            "checkout": "2024-01-29"
        },
        "additionalneeds": "breakfast"
    }
    response = requests.put(url=PUT_URL, headers=headers, json=payload)
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["firstname"] == "Alka"

#delete request
def test_delete():
    URL = "https://restful-booker.herokuapp.com/booking/"
    booking_id = test_create_booking_ID()
    DELETE_URL = URL + str(booking_id)
    cookie_value = "token=" + test_create_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie_value
    }
    print(headers)

    response = requests.delete(url=DELETE_URL, headers=headers)
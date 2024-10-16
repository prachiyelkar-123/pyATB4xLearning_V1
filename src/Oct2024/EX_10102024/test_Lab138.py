#API request
from http.client import responses

import pytest
import allure
import requests


@allure.title("TC#1 - create booking positive")
@allure.description("Verify create booking ID")
@pytest.mark.CRUD

def test_create_booking_ID():
    base_URL = "https://restful-booker.herokuapp.com"
    base_path =  "/booking"
    URL = base_URL + base_path
    headers = {"Content-Type" : "application/json", "Accept" : "application/json"}
    payload ={
        "firstname" : "Prachi",
        "lastname" : "Yelkar",
        "totalprice" : 5000,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2024-01-26",
            "checkout" : "2024-01-30"
        },
        "additionalneeds" : "breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=payload)
    assert response.status_code == 200

    responseData =response.json()

    bookingid = responseData["bookingid"]
    assert bookingid is not None
    assert bookingid > 0
    assert type(bookingid) == int

    firstname = responseData["booking"]["firstname"]
    lastname = responseData["booking"]["lastname"]
    totalprice = responseData["booking"]["totalprice"]
    depositpaid = responseData["booking"]["depositpaid"]
    checkin = responseData["booking"]["bookingdates"]["checkin"]
    checkout = responseData["booking"]["bookingdates"]["checkout"]

    assert firstname == "Prachi"
    assert lastname == "Yelkar"
    assert totalprice == 5000
    assert depositpaid == True
    assert checkin == "2024-01-26"
    assert checkout == "2024-01-30"

@allure.title("TC#2 - create booking negative")
@allure.description("Verify create booking ID")
@pytest.mark.CRUD

def test_create_booking_ID_TC2():
    base_URL = "https://restful-booker.herokuapp.com"
    base_path =  "/booking"
    URL = base_URL + base_path
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    payload = {}
    response = requests.post(url=URL, headers=headers, json=payload)
    assert response.status_code == 500

@allure.title("TC#3 - create booking negative")
@allure.description("Verify create booking ID")
@pytest.mark.CRUD
def test_create_booking_ID_TC3():
    base_URL = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_URL + base_path
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    payload = {
        "firstname": "Prachi",
        "lastname": "Yelkar",
        "totalprice": 5000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-26",
            "checkout": "2024-01-30"
        },
        "additionalneeds": "breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=payload)
    assert response.status_code == 200
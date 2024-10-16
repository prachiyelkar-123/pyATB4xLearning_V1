import pytest
import allure

@allure.title("TC#1 - verify that 5-2 is equel to 4")
@allure.description("This is negative test case")
@pytest.mark.smoke
def test_div_verify_negative():
    assert 5-2 == 4

@allure.title("TC#2 - verify that 5-2 is equel to 3")
@allure.description("This is positive test case")
@pytest.mark.smoke
def test_div_verify_positive():
    assert 5-2 == 3

@allure.title("TC#3 - verify that 5+2 is equel to 7")
@allure.description("This is positive test case of sum")
@pytest.mark.smoke
def test_sum_verify_positive():
    assert 5+2 == 7

@pytest.mark.skip(reason = "do not want to run")
def test_mul_verify_positive():
    assert 5*2 == 10
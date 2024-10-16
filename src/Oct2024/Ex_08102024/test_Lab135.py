import pytest
import allure

def test_test_case_1():
    print("Hello, TC1")

def case_2():
    print("Hello, TC1")

@pytest.mark.reg
def test_test_case_2():
    print("Hello, TC1")

@pytest.mark.reg
def test_div_verify_negative():
    assert 5-2 == 4

@pytest.mark.skip(reason = "don not want to run")
def test_div_verify_positive():
    assert 5-2 == 3
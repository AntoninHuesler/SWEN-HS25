from testing.password import *


def test_password_lenght():
    assert is_password_valid("123") == "password is not valid"

def test_at_least_two_digits():
    assert is_password_valid("Wasserflasche") == "password needs at least 2 digits"
    
def test_at_least_one_capital_letter():
    assert is_password_valid("wasserflasche12") == "password needs at least 1 capital letter"

def test_at_least_one_special_character():
    assert is_password_valid("Wasserflasche12") == "password needs at least 1 special character"
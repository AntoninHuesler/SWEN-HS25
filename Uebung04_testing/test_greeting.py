from Uebung04_testing.greeting import *

def test_return_name():
    assert greet("Bob") == "Hello, Bob"

def test_none():
    assert greet() == "Hello my friend"

def test_uppercase():
    assert greet("BOB") == "HELLO, BOB"

def test_list_0_names():
    assert greet([]) == "Hello my friend"

def test_list_1_name():
    assert greet(["Bob"]) == "Hello, Bob"

def test_list_2_names():
    assert greet(["Bob","Jim"]) == "Hello, Bob and Jim"

def test_list_3_or_more_names():
    assert greet(["Bob","Jim","Linda","Peter"]) == "Hello, Bob, Jim, Linda, and Peter"
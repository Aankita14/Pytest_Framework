import pytest

@pytest.mark.login
def test_m1():
  a = 3
  b = 4
  assert a+1 == b, "Test Failed"
  assert a == b,"Test failed as a is not eq to b"

def test_m2():
    name = "Selenium"
    assert name.upper() == "SELENIUM"

@pytest.mark.login
def test_m3():
    assert True

@pytest.mark.home
def test_m4():
    assert False

def test_m5():
    assert 100 == 100

def test_m6():
    assert "Ankita" == "ANKITA"

@pytest.mark.login
def test_login():
    assert "Admin" == "admin"
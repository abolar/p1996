import pytest
def stub():
    return "OK"

def test_function():
    assert stub() == "OK"
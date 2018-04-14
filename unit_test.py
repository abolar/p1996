import pytest
def stub():
    return "not OK"

def test_function():
    assert stub() == "OK"
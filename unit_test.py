import pytest
def stub():
    return "Not OK"

def test_function():
    assert stub() == "OK"
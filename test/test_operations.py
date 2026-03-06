from src.math_operation import *

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
    
def test_sub():
    assert sub(1, 2) == -1
    assert sub(1, -1) == 2

def test_mul() :
    assert mul(5,5) == 25
    assert mul(5,0) == 0

def test_divide() :
    assert divide(10,2) == 5
    assert divide(10, 5) ==2 
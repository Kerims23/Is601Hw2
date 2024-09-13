''' My Calculator Test '''
from calculator import add, subtract

def test_addition():
    '''
    test that addition function works 
    '''
    assert add(2,2) == 4

def test_subtraction():
    '''
    test that addition function works 
    '''
    assert subtract(2,2) == 0

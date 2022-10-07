import pytest
from src.Triangle import triangle_type



def test_equilateral():
    assert triangle_type(7,7,7) == 'Equilateral'

def test_isosceles():
    assert triangle_type(10,10,4) == 'Isosceles'

def test_scalene():
    assert triangle_type(5,6,7) == 'Scalene'

def test_notTriangle_ab():
    assert triangle_type(1,2,3) == 'Not a triangle'

def test_notTriangle_ac():
    assert triangle_type(3,6,9) == 'Not a triangle'

def test_notTriangle_bc():
    assert triangle_type(1,0,0) == 'Not a triangle'
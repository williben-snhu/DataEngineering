
import rectangle
import pytest

@pytest.mark.parametrize('a,b,result', [(2,4,8),(7,5,35)])
def test_area(a,b,result):
    output=rectangle.area(a,b)
    assert output==result

def test_perimiter():
    output=rectangle.perimiter(2,4)
    assert output==12

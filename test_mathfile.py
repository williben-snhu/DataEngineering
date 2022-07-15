
import mathfile as mf

def test_add():
    output=mf.add(2,3)
    assert output==5

def test_sub():
    output=mf.sub(4,3)
    assert output==1
    
def test_multiply():
    output=mf.multiply(2,3)
    assert output==6

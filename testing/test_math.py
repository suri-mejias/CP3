from equations import (
    add,
    sub,
    mul,
    div
)

def test_add():
    assert add(2,10) == 12
    assert add(3,5) == 8
    assert add(4,6) == 10

def test_sub():
    assert sub(5,1) == 4
    assert sub(10,5) == 5
    assert sub(8,6) == 2

def test_mul():
    assert mul(2,10) == 20
    assert mul(3,5) == 15
    assert mul(4,6) == 24

def test_div():
    assert div(10,2) == 5
    assert div(12,3) == 4
    assert div(4,2) == 2


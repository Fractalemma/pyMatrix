import pytest
from matrix import Matrix

def test_simple():
    A = Matrix()
    A.r = 2
    A.c = 2
    A.matrix = [[1,2],[3,4]]
    B = Matrix()
    B.r = 2
    B.c = 2
    B.matrix = [[1,0],[0,1]]

    C = A.mul(B)

    assert C.r == 2
    assert C.c == 2
    assert C.matrix == [[1,2],[3,4]]

def test_3x3():
    A = Matrix()
    A.r = 3
    A.c = 3
    A.matrix = [[1,2,3],[4,5,6],[7,8,9]]
    B = Matrix()
    B.r = 3
    B.c = 3
    B.matrix = [[1,0,0],[0,1,0],[0,0,1]]

    C = A.mul(B)

    assert C.r == 3
    assert C.c == 3
    assert C.matrix == [[1,2,3],[4,5,6],[7,8,9]]

def test_incompatibleDimensions():
    with pytest.raises(Exception) as exc_info:
        A = Matrix()
        A.r = 3
        A.c = 3
        A.matrix = [[1,2,3],[4,5,6],[7,8,9]]
        B = Matrix()
        B.r = 2
        B.c = 2
        B.matrix = [[1,2],[3,4]]

        C = A.mul(B)

    assert str(exc_info.value) == "Illegal operation: incompatible dimensions"
    
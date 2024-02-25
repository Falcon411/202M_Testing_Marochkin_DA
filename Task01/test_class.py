import pytest

from triangle_class import IncorrectTriangleSides, Triangle


def test_triangle_creation():
    triangle = Triangle(4, 11, 8)
    assert triangle.side_a == 4
    assert triangle.side_b == 11
    assert triangle.side_c == 8


def test_triangle_type_equilateral():
    triangle = Triangle(4, 4, 4)
    assert triangle.triangle_type() == "equilateral"


def test_triangle_type_isosceles():
    triangle = Triangle(4, 7, 4)
    assert triangle.triangle_type() == "isosceles"


def test_triangle_type_nonequilateral():
    triangle = Triangle(4, 11, 8)
    assert triangle.triangle_type() == "nonequilateral"


def test_triangle_creation_negative_side():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(4, -4, 4)


def test_triangle_creation_impossible_triangle():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(4, 4, 11)


def test_triangle_creation_zero_side():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(4, 0, 4)


def test_triangle_perimeter():
    triangle = Triangle(4, 11, 8)
    assert triangle.perimeter() == 23


def test_triangle_perimeter_equilateral():
    triangle = Triangle(4, 4, 4)
    assert triangle.perimeter() == 12

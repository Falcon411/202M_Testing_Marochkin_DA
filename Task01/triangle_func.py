class IncorrectTriangleSides(Exception):
    pass


def get_triangle_type(side_a, side_b, side_c):
    """
    Функция определяет тип треугольника по длинам его сторон.

    Аргументы:
    side_a (float): Длина первой стороны треугольника.
    side_b (float): Длина второй стороны треугольника.
    side_c (float): Длина третьей стороны треугольника.

    Возвращает:
    str: Тип треугольника: "nonequilateral" (разносторонний), "isosceles" (равнобедренный), "equilateral" (равносторонний).

    Примеры:
    >>> get_triangle_type(4, 4, 4)
    'equilateral'

    >>> get_triangle_type(4, 7, 4)
    'isosceles'

    >>> get_triangle_type(4, 11, 8)
    'nonequilateral'

    >>> get_triangle_type(4, -4, 4)
    Traceback (most recent call last):
    ...
    IncorrectTriangleSides: Incorrect side lengths of a triangle

    >>> get_triangle_type(4, 4, 11)
    Traceback (most recent call last):
    ...
    IncorrectTriangleSides: Incorrect side lengths of a triangle

    >>> get_triangle_type(4, 0, 4)
    Traceback (most recent call last):
    ...
    IncorrectTriangleSides: Incorrect side lengths of a triangle
    """
    if side_a <= 0 or side_b <= 0 or side_c <= 0 or side_a + side_b <= side_c or side_b + side_c <= side_a or side_c + side_a <= side_b:
        raise IncorrectTriangleSides("Incorrect side lengths of a triangle")

    if side_a == side_b == side_c:
        return "equilateral"
    elif side_a == side_b or side_b == side_c or side_a == side_c:
        return "isosceles"
    else:
        return "nonequilateral"


if __name__ == "__main__":
    import doctest

    doctest.testmod()

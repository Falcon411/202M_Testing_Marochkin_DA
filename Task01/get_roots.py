import math


def find_roots(a, b, c):
    d = b ** 2 - 4 * a * c

    if a == 0:
        root = -c / b
        return [root]

    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2 * a)
        root2 = (-b - math.sqrt(d)) / (2 * a)
        return sorted([root1, root2])
    elif d == 0:
        root = -b / (2 * a)
        return [root]
    else:
        return []
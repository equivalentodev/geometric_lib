def area(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Стороны прямоугольника должны быть положительными")
    return a * b

def perimeter(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Стороны прямоугольника должны быть положительными")
    return 2 * (a + b)

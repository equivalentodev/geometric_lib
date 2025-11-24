def area(a, h):
    if a <= 0 or h <= 0:
        raise ValueError("Сторона и высота треугольника должны быть положительными")
    return a * h / 2

def perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Стороны треугольника должны быть положительными")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Указанные стороны не образуют треугольник")
    return a + b + c

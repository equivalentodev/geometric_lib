# <span style="color: #98FF98;">geometric_lib</span>

## <span style="color: #ADD8E6;">geometric_lib - python библиотека с базовыми функциями для вычисления площадей и периметров таких фигур, как: круг и квадрат.</span>

![geometry](https://www.litres.ru/book/valentin-butuzov-8681795/geometriya-7-9-klass-68293610/)
---

## <span style="color: #0000FF;">Краткое описание библиотеки</span>
### Использование:

- Чтобы использовать библиотеку, клонируйте данный репозиторий в папку с проектом через команду:
  ```bash
  git clone <ссылка>
  ```

- После импортируйте библиотеку в .py файл следующей командой и приступайте к написанию кода:
    ```python
    from geometric_lib import *
    ```

<p style="color: gray; font-size: 90%;">
<b>Примечание:</b> более подробно расписано в MATHFUNCTIONS.md
</p>

## <span style="color: #0000FF;">Коды функций:</span>
### Круг
```python
import math
def area(r):
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r
```

### Квадрат
```python
def area(a):
    return a * a


def perimeter(a):
    return 4 * a
```

<p style="color: gray; font-size: 90%;">
<b>Примечание:</b> более подробно расписано в .py файлах и папке docs.
</p>

## <span style="color: #0000FF;">Формулы:</span>
|    геометрическая фигура     |      формулы      |
|:----------------------------:|:-----------------:|
|            Круг              |      S = πR²      |
|       Прямоугольник          |      S = ab       |
|           Квадрат            |      S = a²       |
|        Треугольник           |   S = (a * h) / 2 |
---
|    геометрическая фигура     |     формулы       |
|:----------------------------:|:-----------------:|
|            Круг              |      P = 2πR      |
|       Прямоугольник          |   P = 2(a + b)    |
|           Квадрат            |      P = 4a       |
|        Треугольник           |   P = a + b + c   |
<p style="color: gray; font-size: 90%;">
<b>Примечание:</b> более подробно расписано в папке docs.
</p>

## <span style="color: #0000FF;">История коммитов:</span>

```* commit 1095425d722429c28820c5523715105fe5037870
| Author: Mikhail <equivalentoexe@gmail.com>
| Date:   Mon Sep 29 22:13:04 2025 +0300
| 
|     Create new branch and add descriptions for functions in files.
| 
```
# geometriclib
## Общее описание
### geometriclib - библиотека для работы с площадью и периметром кругов, квадратов и треугольников на языке python.
## Функции с примерами вызова
```py
import geometric_lib.circle as circle, geometric_lib.square as square,\
    geometric_lib.triangle as triangle, geometric_lib.triangle as rectangular

circle.area(r) # Площадь круга радиуса r
Circle_ar = circle.area(10) # 314.1592653589793

circle.perimeter(r) # Периметр круга радиуса r
Circle_per = circle.perimeter(10) # 62.83185307179586


square.area(r) # Площадь квадрата со стороной длины a
Square_ar = square.area(10) # 100

square.perimeter(r) # Периметр квадрата со стороной длины a
Square_per = square.perimeter(14) # 100


triangle.area(r) # Площадь треугольника со стороной a, высотой h
Trian_ar = triangle.area(10, 4) # 20.0

trianlge.perimeter(r) # Периметр треугольника со стороной a, высотой h
Trian_per = triangle.perimeter(14, 10, 6) #  30

# Добавлен test_rectangle.py для тестировки
rectangular.area(r) # Площадь прямогольника со сторонами a, b
Rectan_ar = rectangular.area(5, 3) #  15

rectangular.perimeter(r) # Периметр прямогольника со сторонами a, b
Rectan_per = rectangular.perimeter(5, 3) #  16

```
## История изменений
```commit 607448521318bb0e2214c6d74e9625d83693f741 (HEAD -> main, origin/main, origin/HEAD)
Author: Sati Kultueva <satironius@icloud.com>
Date:   Tue Oct 28 19:10:41 2025 +0300

    Update test_rectangle.py

commit 1af9cc81240b44ec00f0785db23d2366392b466b
Author: Sati Kultueva <satironius@icloud.com>
Date:   Tue Oct 28 14:53:01 2025 +0300

    Create test_rectangle.py
```
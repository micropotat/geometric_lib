# geometriclib
## Общее описание
### geometriclib - библиотека для работы с площадью и периметром кругов, квадратов и треугольников на языке python.
## Функции с примерами вызова
```py
import geometric_lib.circle as circle, geometric_lib.square as square,\
    geometric_lib.triangle as triangle

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
```
## История изменений
```commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (upstream/main, upstream/HEAD, docs)
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added
```
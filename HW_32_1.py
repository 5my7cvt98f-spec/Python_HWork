# Класс Rectangle
# Создайте класс Rectangle, который описывает прямоугольник.
# У каждого объекта должны быть два поля: width и height.
# Добавьте метод get_area(), который возвращает площадь прямоугольника.
# Создайте объект прямоугольника с произвольными значениями.
# Выведите его площадь.
# Измените ширину и высоту.
# Выведите новую площадь.


class Rectangle:
    def __init__(self, width, height):
        self.validate(width, height)
        self._width = width
        self._height = height

    def validate(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Ширина и высота должны быть больше 0")

    def get_area(self):
        return self._width * self._height

    def resize(self, width, height):
        self.validate(width, height)

        self._width = width
        self._height = height

        print(f"New rectangle: {self._width} x {self._height}")

    def __str__(self):
        return f"Rectangle({self._width} x {self._height})"


rectangle = Rectangle(3, 4)

print(rectangle)
print("Area:", rectangle.get_area())

rectangle.resize(2, 5)

print(rectangle)
print("New area:", rectangle.get_area())

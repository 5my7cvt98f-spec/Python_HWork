# class Rectangle:
#     def __init__(self, width, height):
#         if width <= 0 or height <= 0:
#             raise ValueError("Ширина и высота должны быть больше 0")

#         self.width = width
#         self.height = height

#     def get_area(self):
#         return self.width * self.height

#     def set_param(self, width, height):
#         if width <= 0 or height <= 0:
#             raise ValueError("Ширина и высота должны быть больше 0")

#         self.width = width
#         self.height = height

#         print(f"New rectangle: {self.width} x {self.height}")


# new_rectangle = Rectangle(3, 4)
# print(new_rectangle.get_area())   # 12

# new_rectangle.set_param(2, 5)
# print(new_rectangle.get_area())   # 10

class Rectangle:
    def __init__(self, width, height):
        self.validate(width, height)

        self._width = width
        self._height = height

    # Проверка данных
    def validate(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Ширина и высота должны быть больше 0")

    # Площадь
    def get_area(self):
        return self._width * self._height

    # Изменение размеров
    def resize(self, width, height):
        self.validate(width, height)

        self._width = width
        self._height = height

        print(f"New rectangle: {self._width} x {self._height}")

    # Красивый вывод объекта
    def __str__(self):
        return f"Rectangle({self._width} x {self._height})"


rectangle = Rectangle(3, 4)

print(rectangle)
print("Area:", rectangle.get_area())

rectangle.resize(2, 5)

print(rectangle)
print("New area:", rectangle.get_area())
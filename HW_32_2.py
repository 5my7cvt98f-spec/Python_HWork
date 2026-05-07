# class Counter:
#     def __init__(self):
#         self.counter = 0  # счётчик начинается с нуля

#     def increment(self):
#         self.counter += 1
#         print(f"После увеличения: {self.counter}")

#     def decrement(self):
#         self.counter -= 1
#         print(f"После уменьшения: {self.counter}")

#     def get_value(self):
#         return self.counter

# # Проверка
# c = Counter()
# c.increment()  # 1
# c.increment()  # 2
# c.increment()  # 3
# c.decrement()  # 2
# print(c.get_value())  # 2


# class Counter:
    
#     def __init__(self):
#         self.counter = 0  # счётчик начинается с нуля
#     def increment(self):
#         self.counter += 1
#         print(f"После увеличения: {self.counter}")
#     def decrement(self):
#         if self.counter == 0:
#             raise ValueError("Счетчик в минус не пойдет")
#         self.counter -= 1
#         print(f"После уменьшения: {self.counter}")
#     def get_value(self):         
#         print(f"текущее значение: {self.counter}")
# # Проверка
# c = Counter()
# c.increment()  # 1
# c.increment()  # 2
# # c.increment()  # 3
# c.decrement()  # 2
# c.get_value()  # 2

class Counter:
    def __init__(self):
        self.value = 0

    # Увеличение счётчика
    def increment(self):
        self.value += 1
        print(f"Значение увеличено, текущее: {self.value}")

    # Уменьшение счётчика
    def decrement(self):
        if self.value <= 0:
            raise ValueError("Счётчик не может быть меньше 0")

        self.value -= 1
        print(f"Значение уменьшено, текущее: {self.value}")

    # Получение текущего значения
    def get_value(self):
        return self.value

    # Красивый вывод объекта
    def __str__(self):
        return f"Counter(value={self.value})"


# Проверка работы

counter = Counter()

counter.increment()   # 1
counter.increment()   # 2
counter.increment()   # 3
counter.increment() 
counter.decrement()   # 2

print("Текущее значение:", counter.get_value())


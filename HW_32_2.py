# Класс Counter
# Реализуйте класс Counter, который представляет собой простой счётчик.
# Счётчик должен начинаться с нуля.
# Предусмотрите методы для увеличения и уменьшения значения на единицу, /
# при этом при каждой операции должно отображаться новое значение счётчика.
# Добавьте метод, возвращающий текущий результат.

# Проверьте работу счётчика, выполнив несколько операций.


class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
        print(f"Значение увеличено, текущее: {self.value}")

    def decrement(self):
        if self.value <= 0:
            raise ValueError("Счётчик не может быть меньше 0")
        self.value -= 1
        print(f"Значение уменьшено, текущее: {self.value}")

    def get_value(self):
        return self.value

    def __str__(self):
        return f"Counter(value={self.value})"


counter = Counter()

counter.increment()
counter.increment()
counter.increment()
counter.increment()
counter.decrement()

print("Текущее значение:", counter.get_value())

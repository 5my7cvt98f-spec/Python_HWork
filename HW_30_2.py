"""
Генератор уникальных элементов
Создайте генератор, который принимает список элементов и выдаёт только уникальные значения, сохраняя порядок их появления в исходном списке.
Данные:
data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]
Пример вывода:
3
1
2
4
5
6
7
8
"""


def get_unique_elements(data):
    seen = set()
    for item in data:
        if item not in seen:
            seen.add(item)
            yield item


data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]

for value in get_unique_elements(data):
    print(value)
"""
Комбинации одежды
Напишите функцию, которая принимает списки типов одежды,
цветов и размеров, а затем генерирует все возможные
комбинации в формате "Clothe - Color - Size".

Данные:
    clothes = ["T-shirt", "Jeans", "Jacket"]
    colors = ["Red", "Blue", "Black"]
    sizes = ["S", "M", "L"]
    Пример вывода:
    T-shirt - Red - S
    T-shirt - Red - M
    T-shirt - Red - L
    T-shirt - Blue - S
    ...
    Jacket - Black - L

"""


def generate_combinations(clothes, colors, sizes):
    for cloth in clothes:
        for color in colors:
            for size in sizes:
                yield f"{cloth} - {color} - {size}"


clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]

for combo in generate_combinations(clothes, colors, sizes):
    print(combo)
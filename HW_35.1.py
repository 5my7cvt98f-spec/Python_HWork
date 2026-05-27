"""
Предсказание пола по имени

Изучите документацию API предсказания пола по имени:
https://genderize.io/documentation/api/reference
Напишите программу, которая запрашивает имя пользователя
и выводит его пол и вероятность этого предсказания.

Пример ввода:
    Введите имя: Sasha

Пример вывода:
    Предполагаемый пол: female
    Вероятность: 59.0%
"""

import requests

name = "Svitlana"

response = requests.get("https://api.genderize.io", params={"name": name})
data = response.json()

print(f"Предполагаемый пол: {data.get('gender')}")
print(f"Вероятность: {data.get('probability') * 100:.1f}%")

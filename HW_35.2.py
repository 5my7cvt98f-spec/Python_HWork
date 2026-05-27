"""
Получение биржевых данных через API

Напишите программу, которая запрашивает у
пользователя тикер (symbol) акций, обращается
к функции с помесячными данными о результатах
торгов (TIME_SERIES_MONTHLY) в API ресурса www.alphavantage.co,
запрашивает результат в формате csv, записывает его в файл.
Доступность ресурса предварительно нужно проверить.
После этого файл требуется прочитать, извлечь данные
из столбца volume и вычислить среднее значение этого столбца.

Пример ввода:
    Введите тикер: BMWYY

Пример вывода:
    CSV-файл успешно сохранён
    Средний объём: 7638446.53

https://www.alphavantage.co/documentation/
"""

import requests
import csv
import sys


API_KEY = "TWL069HQZFTF1EQI"
symbol = "BMWYY"
api_url = "https://www.alphavantage.co/query"

params = {
    "function": "TIME_SERIES_MONTHLY",
    "symbol": symbol,
    "datatype": "csv",
    "apikey": API_KEY,
}

response = requests.get(api_url, params=params, timeout=20)
if response.status_code != 200:
    print("API недоступен")
    sys.exit()

with open(filename := f"{symbol}_monthly.csv", "w", encoding="utf-8", newline="") as f:
    f.write(response.text)

with open(filename, "r", encoding="utf-8", newline="") as f:
    volumes = [float(row["volume"]) for row in csv.DictReader(f) if row["volume"]]

print(f"Средний объём: {sum(volumes) / len(volumes):.2f}")

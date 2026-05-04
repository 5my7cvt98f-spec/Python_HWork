import csv
import statistics

# Список предметов
subjects = ["Science", "Math", "Physics"]

# Словарь для хранения оценок
grades_data = {
    "Science": [],
    "Math": [],
    "Physics": []
}

# Читаем исходный файл
with open("lesson_60/grades.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    # Создаём файлы по предметам
    output_files = {}
    writers = {}

    for subject in subjects:
        output_file = open(
            f"grades-{subject}.csv",
            "w",
            newline="",
            encoding="utf-8"
        )

        output_files[subject] = output_file

        writer = csv.writer(output_file)
        writers[subject] = writer

        # Заголовки
        writer.writerow(["name", "grade"])

    # Обрабатываем строки
    for row in reader:

        subject = row["subject"]

        # Берём только нужные предметы
        if subject in subjects:

            name = row["name"]
            grade = int(row["grade"])

            # Запись в отдельный файл
            writers[subject].writerow([name, grade])

            # Сохраняем оценку
            grades_data[subject].append(grade)

    # Закрываем файлы
    for file in output_files.values():
        file.close()

# Создаём файл статистики
with open("grades-info.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow([
        "subject",
        "average",
        "min",
        "max",
        "median",
        "std_dev"
    ])

    # Статистика
    for subject in subjects:

        grades = grades_data[subject]

        writer.writerow([
            subject,
            round(statistics.mean(grades), 2),
            min(grades),
            max(grades),
            statistics.median(grades),
            round(statistics.stdev(grades), 2)
        ])

print("Файлы успешно созданы!")
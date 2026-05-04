import json
from datetime import datetime

# Открываем JSON-файл
with open("student_courses.json", "r", encoding="utf-8") as file:
    students = json.load(file)

# Общее количество студентов
total_students = len(students)

# Сумма возрастов на момент поступления
total_age = 0

for student in students:
    # Дата рождения
    birth_date = datetime.strptime(student["birth_date"], "%d.%m.%Y")

    # Дата поступления
    enrollment_date = datetime.strptime(student["enrollment_date"], "%d.%m.%Y")

    # Вычисляем возраст
    age = enrollment_date.year - birth_date.year

    # Проверяем, был ли уже день рождения
    if (
        enrollment_date.month,
        enrollment_date.day
    ) < (
        birth_date.month,
        birth_date.day
    ):
        age -= 1

    total_age += age

# Средний возраст
average_enrollment_age = round(total_age / total_students, 1)

# Формируем отчёт
report = {
    "total_students": total_students,
    "average_enrollment_age": average_enrollment_age
}

# Сохраняем отчёт в новый JSON-файл
with open("student_courses_report.json", "w", encoding="utf-8") as file:
    json.dump(report, file, ensure_ascii=False, indent=4)

print("Отчёт успешно создан!")
import json
def read_students():
    try:
        file = open("students.json", "r", encoding="utf-8")
        students = json.load(file)
        file.close()
        return students
    except FileNotFoundError:
        print("Ошибка: файл students.json не найден.")
        return []

def make_report(students):
    report = {}
    report["students"] = []
    all_grades = []
    for student in students:
        if "name" not in student or "grades" not in student:
            print("Ошибка: нет ключа name или grades.")
            continue
        name = student["name"]
        grades = student["grades"]
        if type(name) != str or type(grades) != list:
            print("Ошибка: неверный тип данных у ученика(цы)", name, ".")
            continue
        if len(grades) == 0:
            print("Ошибка: список оценок", name, "пустой.")
            continue
        all_ints = True
        for i in grades:
            if type(i) != int:
                all_ints = False
                break
        if not all_ints:
            print("Ошибка: оценки", name, "должны быть целыми числами.")
            continue

        average = sum(grades) / len(grades)
        student_result = {}
        student_result["name"] = name
        student_result["average_grade"] = round(average, 2)
        report["students"].append(student_result)
        all_grades = all_grades + grades
    if len(all_grades) > 0:
        report["overall_average"] = round(sum(all_grades) / len(all_grades), 2)
    else:
        report["overall_average"] = 0
    return report

def save_report(report):
    file = open("report.json", "w", encoding="utf-8")
    json.dump(report, file, ensure_ascii=False, indent=4)
    file.close()
    print("Отчёт сохранён в report.json")
students = read_students()

if len(students) > 0:
    report = make_report(students)
    save_report(report)

print('#Задание 1')
employed = input("Вы трудоустроены? (True/False): ")
vacation = input("Вы в отпуске? (True/False): ")
if employed and vacation:
    print(True)
else:
    print(False)

print("_________________________________________________________")
print('#Задание 2')
operation = input("Введите операцию (+, -, *, /): ")
value_1 = int(input("Введите первое число: "))
value_2 = int(input("Введите второе число: "))
if operation == "+":
    print(value_1 + value_2)
elif operation == "-":
    print(value_1 - value_2)
elif operation == "*":
    print(value_1 * value_2)
elif operation == "/":
    if value_2 == 0:
        print("Нельзя днлить на ноль!")
    else:
        print(value_1 // value_2)

print("_________________________________________________________")
print("#Задание 3")
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a > b:
    a, b = b, a
summa = 0
for i in range(a, b + 1):
    summa += i

print("Сумма:", summa)

print("_________________________________________________________")
print("#Задание 4")
month = int(input("Введите номер месяца (1-12): "))

if month < 1 or month > 12:
    print("Неверный номер месяца")
else:
    if month <= 3:
        kvartal = 1
    elif month <= 6:
        kvartal = 2
    elif month <= 9:
        kvartal = 3
    else:
        kvartal = 4
    if month == 12 or month == 1 or month == 2:
        season = "Зима"
    elif month >= 3 and month <= 5:
        season = "Весна"
    elif month >= 6 and month <= 8:
        season = "Лето"
    else:
        season = "Осень"

    print("Квартал:", kvartal)
    print("Время года:", season)
print("_________________________________________________________")
print("#Задание 5")
total = 0
count = 0

while True:
    ocenka = int(input("Введите оценку (-1 для завершения): "))
    if ocenka == -1:
        break
    total += ocenka
    count += 1

if count == 0:
    print("Оценки не введены")
else:
    ball = total / count
    if ball >= 90:
        print("Оценка: A")
    elif ball >= 80:
        print("Оценка: B")
    elif ball >= 70:
        print("Оценка: C")
    elif ball >= 60:
        print("Оценка: D")
    else:
        print("Оценка: F")
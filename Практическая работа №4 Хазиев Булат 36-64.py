print("#Задание1")
def calc(operation, value1, value2):
    if operation == '+':
        return value1 + value2
    elif operation == '-':
        return value1 - value2
    elif operation == '*':
        return value1 * value2
    elif operation == '/':
        if value2 == 0:
            print("Нельзя делить на ноль!")
        return value1 / value2
    else: return("Операция не найдена")

operation = input('Введите операцию(+,-,*,/):')
value1 = int(input('Введите первое число:'))
value2 = int(input('Введите второе число:'))
print( calc(operation, value1, value2))

print("_________________________________________________________")
print("#Задание 2")
def quart(month):
    if 1 <= month <= 3:
        return 1
    elif 4 <= month <= 6:
        return 2
    elif 7 <= month <= 9:
        return 3
    elif 10 <= month <= 12:
        return 4
    else:
        return None


def season(month):
    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    elif month in [9, 10, 11]:
        return "Осень"
    else:
        return None


month = int(input("Введите номер месяца (1-12): "))

quart = quart(month)
season = season(month)

if quart:
    print("Квартал:", quart)
    print("Сезон:", season)
else:
    print("Ошибка: такого месяца нет")

print("_________________________________________________________")
print("#Задание 3")
def symvols(sentence, symbols):
    counts = {}
    for symbol in symbols:
        counts[symbol] = sentence.count(symbol)
    return counts

sentence = input("Ввведите предложение: ")
symbols = input("Введите символыы для подсчёта: ")
result = symvols(sentence, symbols)

for symbol, count in result.items():
    print(f"Символ '{symbol}' встречается {count} раз")

print("_________________________________________________________")
print("#задание 4")
def counts(text):
    count = 0
    for sym in text:
        if 'm' <= sym<= 'z':
            count += 1
    return count


text = input("Введите строку из букв от a до z: ")
print("Количество символов от m до z:", counts(text))
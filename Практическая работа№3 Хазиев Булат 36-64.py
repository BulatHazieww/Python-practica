print("# Задание 1")
words = ["Яблоко", "Груша", "Слива", "Банан", "Апельсин", "Виноград"]

search_word = input("Введите слово для поиска: ")
for i in range(len(words)):
    if words[i] == search_word:
        print('Индекс:', i)
        break
else:print('Строка не найдена')


print("_________________________________________________________")
print("# Задание 2")
numbers = [5, 7, 6, 7, 9, 9, 7]
new_numbers = []

for element in numbers:
    if element not in new_numbers:
        new_numbers.append(element)

print("Список без дубликатов:", new_numbers)


print("_________________________________________________________")
print("# Задание 3")
lst = ['a', 'b', 'c', 'a', 'd', 'd', 'a', 'e']

counter_dict = {}
for element in lst:
    counter_dict[element] = counter_dict.get(element, 0) + 1

for key, value in counter_dict.items():
    print(key, ':', value)
print("_________________________________________________________")
print("#Заданине 4")
spisok = [5, -7, 8.9, 10, 6, -10, 3.14]

mi =10**10

for x in spisok:
    if isinstance(x, int) and x < mi:
        mi = x
spisok.remove(mi)

print(spisok)
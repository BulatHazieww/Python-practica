print("Задание 1")
n = int(input("Введите количество человек (n): "))
if n <= 0:
    print("Количество человек должно быть больше 0.")
else:
    total_age = 0

    for i in range(1, n + 1):
        age = int(input(f"Введите возраст человека №{i}: "))
        total_age += age

    average_age = total_age / n
    print(f"Средний возраст: {average_age}")


print("________________________________________________________")
print("задание 2")
code = input().strip()
if code == "000000":
    print("черный")
elif code == "ffffff":
    print("белый")
else:
    r_hex = code[0:2]
    g_hex = code[2:4]
    b_hex = code[4:6]
    r = int(r_hex, 16)
    g = int(g_hex, 16)
    b = int(b_hex, 16)
    if r == g == b:
        print("серый")
    else:
        if r >= g and r >= b:
            print("красный")
        elif g >= r and g >= b:
            print("зелёный")
        else:
            print("синий")

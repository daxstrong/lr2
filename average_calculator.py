# Инициализация пустого списка для чисел
numbers = []

# Запрашиваем у пользователя количество чисел, которые он хочет ввести
count = int(input("Введите количество чисел: "))

# Запрашиваем числа у пользователя и добавляем их в список
for i in range(count):
    num = float(input(f"Введите число {i+1}: "))
    numbers.append(num)

# Вычисляем сумму чисел
total = sum(numbers)

# Вычисляем среднее арифметическое
average = total / count

# Выводим результат на экран
print(f"Сумма чисел: {total}")
print(f"Среднее арифметическое: {average}")

# Выводим результат на экран
print(f"Сумма чисел: {total}")
print(f"Среднее арифметическое: {average}")
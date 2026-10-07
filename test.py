# 1
# month = int(input("Введите номер месяца: "))

# months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
#           "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]

# if 1 <= month <= 12:
#     print(months[month - 1])
# else:
#     print("Неверный номер месяца")
# 2
# for i in range(100, 201):
#     print(i)
# 3
# best = None
# n = 1

# while True:
#     time = float(input(f"Спортсмен {n}: "))
#     if time <= 0:
#         break
#     if best is None or time < best:
#         best = time
#     print(f"Лучший результат: {best} сек\n")
#     n += 1

# 4
# target = 237

# # Из 237 получаем первую цифру (она же последняя цифра искомого числа)
# c = target // 100  # первая цифра числа 237
# remainder = target % 100  # остаток (37)

# # remainder = 10a + b, где a и b - первые две цифры искомого числа
# a = remainder // 10
# b = remainder % 10

# # Составляем искомое число
# found_number = 100 * a + 10 * b + c

# print(f"Из уравнения c*100 + 10a + b = {target}:")
# print(f"  c (последняя цифра) = {c}")
# print(f"  10a + b = {remainder}")
# print(f"  a (первая цифра) = {a}")
# print(f"  b (вторая цифра) = {b}")
# print(f"\nИскомое число: {found_number}")

# # Проверка
# last_digit = found_number % 10
# result = found_number - last_digit
# quotient = result // 10
# new_number = int(str(last_digit) + str(quotient))

# print(f"\nПроверка:")
# print(f"  {found_number} - {last_digit} = {result}")
# print(f"  {result} / 10 = {quotient}")
# print(f"  {last_digit} приписываем слева к {quotient}: {new_number}")
# print(f"  Результат: {new_number} {'✓' if new_number == 237 else '✗'}")

# print("\n" + "="*50)
# print(f"\nОТВЕТ: Искомое число = {found_number}")

# 5
# number = int(input("Введите двузначное число: "))
# tens = number // 10
# ones = number % 10
# digit_sum = tens + ones
# digit_product = tens * ones


# print(f"\nЧисло: {number}")
# print(f"а) Десятки: {tens}")
# print(f"б) Единицы: {ones}")
# print(f"в) Сумма: {digit_sum}")
# print(f"г) Произведение: {digit_product}")

# 6

# birth_year = int(input("Введите год рождения: "))
# birth_month = int(input("Введите месяц рождения (1-12): "))
# current_year = int(input("Введите текущий год: "))
# current_month = int(input("Введите текущий месяц (1-12): "))

# age = current_year - birth_year

# if current_month < birth_month:
#     age = age - 1

# print(f"\nВозраст человека: {age} полных лет")

# 7
# number = float(input("Введите число: "))
# if number > 5:
#     number = number + 20
#     print(f"Число больше 5, увеличиваем на 20")
# else:
#     number = number - 15
#     print(f"Число не больше 5, уменьшаем на 15")
# print(f"Результат: {number}")

# 8

# number = float(input("Введите число: "))
# if number < 177:
#     print("Число меньше 177")

# if number > 105:
#     print("Число больше 105")

# 9

# day_number = int(input("Введите номер дня недели (1-7): "))

# if day_number == 1:
#     print("Понедельник")
# elif day_number == 2:
#     print("Вторник")
# elif day_number == 3:
#     print("Среда")
# elif day_number == 4:
#     print("Четверг")
# elif day_number == 5:
#     print("Пятница")
# elif day_number == 6:
#     print("Суббота")
# elif day_number == 7:
#     print("Воскресенье")
# else:
#     print("Ошибка: введите число от 1 до 7")

# 10
# a = float(input("Введите первое число: "))
# b = float(input("Введите второе число: "))

# if a > b:
#     print(f"Наибольшее число: {a}")
# else:
#     print(f"Наибольшее число: {b}")

# 11

# a = float(input("Введите первое число: "))
# b = float(input("Введите второе число: "))

# if abs(a - b) == 100:
#     print("Числа отличаются на 100")
# else:
#     print("Числа на 100 не отличаются")

# 12
# a = float(input("Введите первое число: "))
# b = float(input("Введите второе число: "))

# if a > b:
#     print("Первое число больше второго")
# elif a == b:
#     print("Числа равны")
# else:
#     print("Второе число больше первого")

# 13

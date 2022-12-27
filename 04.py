# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

user_number = int(input("Введите целое число: "))
result = []

while user_number != 1:
    result.append(user_number % 2)
    user_number = user_number // 2
result.append(1)
result.reverse()
print(result)
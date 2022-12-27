# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

user_number = int(input("Введите число: "))

def positive_fibonacci(num):
    positive_list = [0, 1]
    for i in range(num - 1):
        positive_list.append(positive_list[-2] + positive_list[-1])
    return positive_list

def negative_fibonacci(num):
    negative_list = [0, 1]
    for i in range(num - 1):
        negative_list.append(negative_list[-2] - negative_list[-1])
    return negative_list[::-1]

print(negative_fibonacci(user_number) + positive_fibonacci(user_number))
 
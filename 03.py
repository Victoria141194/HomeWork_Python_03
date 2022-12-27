# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.

import random
first_list = [round(random.uniform(0, 10), 2) for i in range (random.randint(4, 10))]
print(first_list)

second_list = []

for i in first_list:
    second_list.append(round(i % 1, 2))
print(second_list)

max = second_list[0]
min = second_list[0]

for i in second_list:
    if i > max: max = i
    if i < min: min = i

print(max - min)
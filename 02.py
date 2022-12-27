# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

list = [3, 6, 2, 7, 5]
result = []

if len(list) % 2 != 0:
    for i in range(len(list) // 2 +1) :
        result.append(list[i] * list[-i-1])
else:
    for i in range(len(list) // 2): 
       result.append(list[i] * list[-i-1])
print(result)
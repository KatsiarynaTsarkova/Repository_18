import random
#Задача 2. Дан список случайных чисел. Создайте список, в который 
# попадают числа, описывающие случайную возрастающую последовательность.
# Порядок элементов менять нельзя.
#[1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.
lst = [1, 5, 2, 3, 4, 6, 1, 7]
index = random.randint(0, 7)
result = [lst[index]]
print(result)
while index < 7:
    index = random.randint(index, 7)
    if index != 7 and lst[index] > result[-1]:
        result.append(lst[index])
print(result)        
        
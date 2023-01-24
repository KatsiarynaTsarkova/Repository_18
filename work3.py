import random
#Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов 
# есть в списке. Удалите все повторяющиеся элементы.
#[1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадаютСписок уникальных элементов
#[1, 4, 2, 3, 6, 7]
numbers = list(random.randint(1, 10) for _ in  range(8))
print(numbers)
for el in numbers:
    count = 0
    if el == el:
        count +=2
print(f'{count} элементов совпадают') 
result = set(numbers)
result = list(result)
print(result) 
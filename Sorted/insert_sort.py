#
# Сортировка массива вставками
#
import random as r


# Создание массива
i = 0
len = 2
array = []
while i < len:
    array.append(r.randint(-1000,1000))
    i = i + 1
print('Исходный массив: \n',array)

# Цикл начинаем с 1-го элемента, так как нулевой физически не может иметь предыдущего
for i in range(1,len):
    # -1 в range говорит о том, что мы идём на уменьшение с шагом 1 (10, 9, 8 ...)
    for k in range(i, 0, -1):
        if array[k] < array[k-1]:
            # Обмен текущего элемента и предыдущего между собой
            array[k], array[k-1] = array[k-1], array[k]
        else:
            break
print('Массив после сортировки: \n', array)

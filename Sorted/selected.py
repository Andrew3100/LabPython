# Сортировка выборкой
import random as r


# Создание массива
i = 0
l = 5
array = []
while i < l:
    array.append(r.randint(-1000,1000))
    i = i + 1
print('Исходный массив: \n',array)


for i in range(l-1):
    # запоминаем текущее значение во временную переменную
    m = array[i]
    # запоминаем индекс текущего значения
    p = i
    # поиск минимального среди оставшихся элементов
    for j in range(i+1, l):
        if m > array[j]:
            m = array[j]
            p = j
    if p != i:          # обмен значениями, если был найден минимальный не в i-й позиции
        temp = array[i]
        array[i] = array[p]
        array[p] = temp

print('Отсортированный массив: \n',array)
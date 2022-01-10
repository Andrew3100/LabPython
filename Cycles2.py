

# Вводить числа вручную пока не попадётся число 0. Чётные и нечётные числа массива записывать в разные списки.
# Пройти циклом оба списка и вычислить разницу между элементами первого и второго списков

# Вводим до нуля
# Значение любое, кроме строкового нуля - Python не позволяет использовать необъявленные переменные
inp = 0
input_array = []
chet = []
non_chet = []
# Пока inp не равно нулю (переформатированному в строку)
while inp != str(0):
    # Пересоздаём наш inp
    inp = str(input('Введите элемент: '))
    if inp != str(0):
        # А то, что ввели пишем в массив
        input_array.append(inp)

# Перебор массива
for i in range(0, len(input_array)):
    # Получаем два массива с чётными и нечётными числами
    if int(input_array[i]) % 2 == 0:
        chet.append(input_array[i])
    else:
        non_chet.append(input_array[i])

print(chet)
print(non_chet)

razn = []
for i in range(0, len(chet)):
    razn.append(int(chet[i]) - int(non_chet[i]))
print(razn)





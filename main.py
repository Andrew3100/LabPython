import random as rnd

input_array = []

# Вводим до нуля
# Значение любое, кроме строкового нуля - Python не позволяет использовать необъявленные переменные
inp = 0
# Пока inp не равно нулю (переформатированному в строку)
while inp != str(0):
    # Пересоздаём наш inp
    inp = str(input('Введите элемент: '))
    if inp != str(0):
        # А то, что ввели пишем в массив
        input_array.append(inp)














# ограничиваем ввод числом
# for i in range(0,3):
#     inp = input('Введите элемент ' + str(i)+ ': ')
#     input_array.append(())
#     if inp == 0:
#         break
# print(input_array)

















# Рандомизированный ввод


# # Имена игроков
# names = ['Андрей', 'Максим', 'Олег', 'Иван', 'Алексей']
#
# # Массив счетов
# # Объявляем пустой массив
# score = []
# n = 0
# for i in range(0, 5):
#     score.append(n)
#     n += 10
#
# # names - массив игроков
# # score - массив счетов
# random_name = []
# for g in range(0, 5):
#     # Берём случайное имя
#     # Берём случайное имя
#     # randint(0,n) - берёт целое число в указанном диапазоне
#     # + соединяет строки между собой
#     # names[rnd.randint(0, len(names)-1)] - имя игрока, случайное
#     # + '_' + добавляем разделитель
#     # str(score[rnd.randint(0, len(score)-1)]) строковое значение счёта
#     random_name.append ( names[rnd.randint(0, len(names)-1)] + '_' + str(score[rnd.randint(0, len(score)-1)]) )














# Отдельный массив имён
name = []
# Отдельный массив счетов
score = []

for i in range(0, len(input_array)):
    # В массив name пишем знчения имён
    name.append(input_array[i].split(sep='_')[0])
    # В массив core пишем знчения счетов
    score.append(input_array[i].split(sep='_')[1])

# print(name)
# print(score)

dictionary = {}
for i in range(0, len(score)):
    current_name = name[i]
    person_score = 0
    # В цикле мы считаем значение счёта по всем играм каждого игрока
    for k in range(0, len(name)):
        if name[k] == current_name:
            person_score = person_score + int(score[k])
    dictionary[current_name] = person_score
print(dictionary)
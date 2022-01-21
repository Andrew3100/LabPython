import random as r



names = ['Андрей', 'Алексей', 'Иван', 'Илья', 'Татьяна', 'Александр', 'Олег', 'Анатолий', 'Пётр', 'Максим'];


# 1) Дан массив из 10 имён. Необходимо сформировать 10000 записей о результатах некоторой игры.
# Запись представляет из себя элемент массива (пару ключ-значение), в котором содержится ник игрока
# и количество набранных им очков. Сформированный массив вывести на экран.

niks = []
scores = []
for i in range(0, 10000):
    niks.append(names[r.randint(0,len(names))-1] + str(r.randint(0, 5000)))
    scores.append(r.randint(0, 10000))

result = {}


for i in range(0, len(niks)):
    result[niks[i]] = scores[i]



keys = list(result.keys())
values = list(result.values())

for i in range(0, len(keys)):
    print('Игрок ' + str(keys[i]) + ' набрал ' + str(values[i]) + ' очков')






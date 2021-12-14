import random as rnd


# Имена игроков
names = ['Андрей', 'Максим', 'Олег', 'Иван', 'Алексей']
# Массив счетов
score = []
n = 0
for i in range(0, 10):
    score.append(n)
    n += 10


random_name = []
for g in range(0, 10):
    # Берём случайное имя. Чтобы не повторить имя игрока - к нику добавляем случайные цифры
    random_name.append(names[rnd.randint(0, len(names)-1)] + '_' + str(score[rnd.randint(0, len(score)-1)]))

# Список случайных имён с количеством набранных очков
print(random_name)

# Отдельный массив имён
name = []
# Отдельный массив счетов
score = []
for i in range(0, len(random_name)):
    name.append(random_name[i].split(sep='_')[0])
    score.append(random_name[i].split(sep='_')[1])

print(name)
print(score)


dictionary = {}
for i in range(0, len(score)):
    current_name = name[i]
    person_score = 0
    for k in range(0, len(name)):
        if name[k] == current_name:
            person_score += int(score[k])
    dictionary[current_name] = person_score
print(dictionary)
# Получаем самое короткое слово
def sam_korot(s):
    w = ''
    # Принимаем самое короткое слово большим
    minw = 'x' * 999
    i = 0
    while i < len(s):
        # Пока не дошли до границы слова
        while (i < len(s)) and (s[i] != ' '):
            # Считываем слово
            w = w + s[i]
            i = i + 1
        # Считали его
        else:
            if len(w) < len(minw):
                minw = w
            # Пропускаем пробелы
            while (i < len(s)) and (s[i] == ' '):
                i = i + 1
            w = ''
    # Считываем новое слово
    if (minw != 'x' * 999):
        return minw

# Удаляем из строки слово
def remove(s, endd):
    # Обозначим результирующую строку
    res = ''
    w = ''
    i = 0
    while i < len(s):
        # Пока не дошли до границы слова
        while (i < len(s)) and (s[i] != ' '):
            # Считываем слово
            w = w + s[i]
            i = i + 1
        # Считали его
        else:
            # Идем до пробелов, которые надо удалить
            while (i < len(s)) and (s[i] == ' '):
                i = i + 1
            # Если слово совпадает с заданным
            if w != endd:
                # Добавляем считанное слово к строке
                res = res + w + ' '
                w = ''
    # Читаем следующее слово
    return res

s = input('Введите строку: ')
# Переменная строки слов
arr = ''
# Пока не разобрана вся строка
while s != '':
    # Получаем самое короткое слово..
    endd = sam_korot(s)
    # .. и удаляем его из строки
    s = remove(s, endd)
    # Возвращаем самое короткое слово в перемнную строки слов
    arr = arr + endd	 + ' '
print('Слова по возрастанию длины:', arr)
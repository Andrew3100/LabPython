# Поиск минимального


def search_min():
    array = ['2','5','10','','1','16','7']

    min = len(array[0])
    for i in range(0,len(array)):
        print('Минимум на текущем шаге', min)
        if len(array[i]) < min:
            min = len(array[i])

    return min

sam_korot = search_min()
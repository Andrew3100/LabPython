# Поиск минимального


def search_min(array):
    min = len(array[0])
    for i in range(0,len(array)):
        print('Минимум на текущем шаге', min)
        if len(array[i]) < min:
            min = len(array[i])

    return min
array = ['2','5','10','','1','16','7']
sam_korot = search_min(array)
print(sam_korot)
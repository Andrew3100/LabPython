# Поиск минимального

# Наша строка
string = '123 22'


def search_min_in_string(string):
    i = 0
    # sam_korot = 0
    while i <= len(string)-1:
        word = ''
        while string[i] != ' ':
            word = word + string[i]
            i = i + 1
    print(word)




#
# def search_min(array):
#     min = len(array[0])
#     for i in range(0,len(array)):
#         print('Минимум на текущем шаге', min)
#         if len(array[i]) < min:
#             min = len(array[i])
#     return min

(search_min_in_string(string))

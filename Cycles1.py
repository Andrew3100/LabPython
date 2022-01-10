

# Дан текст. В каждом слове вычислить количество согласных и гласных букв и вывести на экран

# Ввод строки пользователем
string = str(input())

string_array = string.split(' ')

# получили список слов нашего предложения
print(string_array)
# Массив гласных
vowels = ['а', 'о', 'у', 'э', 'ы', 'я', 'ё', 'ю', 'у', 'и', 'е']

# Перебор массива
for i in range(0, len(string_array)):
    vowels_text_count = []
    non_vowels_text_count = []
    # string_array[i] - текущее слово в нашем массиве
    for g in range(0, len(string_array[i])):
         # string_array[i][g] - отдельно взятая буква слова, например string_array[1][2] - буква ж для текста "В каждом слове вычислить количество согласных и гласных букв и вывести на экран"
         if string_array[i][g] in vowels:
             vowels_text_count.append(string_array[i][g])
         else:
             non_vowels_text_count.append(string_array[i][g])
    print('В слове ' + str(string_array[i]) + ' согласных букв - ' + str(len(non_vowels_text_count)) + ', а гласных - ' + str(len(vowels_text_count)))


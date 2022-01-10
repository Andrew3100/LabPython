
string = str(input())

array = string.split(' ')

vowels = ['а', 'о', 'у', 'э', 'ы', 'я', 'ё', 'ю', 'у', 'и', 'е']

for i in range(0, len(array)):
    vowels_text_count = []
    non_vowels_text_count = []
    for g in range(0, len(array[i])):
        if array[i][g] in vowels:
            vowels_text_count.append(array[i][g])
        else:
            non_vowels_text_count.append(array[i][g])
    print('В слове ' + str(array[i]) + ' согласных букв - ' + str(len(non_vowels_text_count)) + ', а гласных - ' + str(len(vowels_text_count)))

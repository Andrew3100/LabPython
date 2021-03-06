



def my_min(*args):

    result = args[0]
    for num in args:
        if num < result:
            result = num
    return result

print(my_min([4, 5, 6, 7, 1,-3,-8,-10]))






exit()
# Используя стандартные средства. Кратчайший вариант
string = str(input('Введите строку: '))
string = string.split(' ')
# sorted - сортирует массив по возрастанию, если целые числа. Если строк - учитывается возрастание длин
print(sorted(string))

# Собственная реализация. Сортировка пузырьком
def sort_array_bubble(arr):
    # Изначально ставим флаг в правду, чтобы цикл начал выполняться
    flag = True
    # Пока флаг
    while flag:
        # Ставим неправдой на случай, если условие не выполнится
        flag = False
        # Перебор массива
        for i in range(len(arr) - 1):
            # Если текущий элемент больше следующего по позиции индекса. Если не выполняется, то массив отсортирован правильно
            if arr[i] > arr[i + 1]:
                # То на место текущего элемента ставим следуюущий, и соответственно, наоборот
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                # Ставим флаг в правду, чтобы запустить следующую итерацию.
                flag = True
    return arr

# Алгоритм сортировки выборкой
def select(arr):
    # i это количество значений которое мы отсортировали
    for i in range(len(arr)):
        # Изначально берём наименьшим первый элемент исходного массива
        lowest_value_index = i
        # цикл начиная после значения i - перебирает элементы, которые ещё не отсортированы
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[lowest_value_index]:
                lowest_value_index = j
        # Самый маленький элемент меняем с первым в списке
        arr[i], arr[lowest_value_index] = arr[lowest_value_index], arr[i]
    return arr

# Сортировка вставкой
def insertion_sort(arr):
    # По правилам метода вставки начинаем сортировать со второго по счёту элемента
    for i in range(1, len(arr)):
        item_to_insert = arr[i]
        # В переменной j будет храниться ссылка на предыдущий индекс для сравнения
        j = i - 1
        # пока предыдущий индекс нулевой и больше (признак того, что предыдущая замена не прошла - сегмент уже отсортирован) и сам предыдущий элемент больше текущего, проиводим замену и уменьшение индекса
        while j >= 0 and arr[j] > item_to_insert:
            arr[j + 1] = arr[j]
            j -= 1
        # Вставка элемента
        arr[j + 1] = item_to_insert
    return arr

# Ввод
string = str(input('Введите строку: '))

# Делим по пробелам
arr = string.split(' ')

# arr = sort_array_bubble(arr)

# arr = select(arr)

arr = insertion_sort(arr)
# Вывод листа для сверки
print(arr)
# Цикл формирования строки
s = ''
for i in range(0, len(arr)):
    s = s + ' ' + str(arr[i])
# Вывод строки для сверки
print(s)
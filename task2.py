#   Дан массив из значений. Каждое значение представляет из себя номер столика в ресторане, размер
#   счёта, оставленного за столиком, а также дату - 6 цифр. Первые две цифры даты являются днём (1-30),
#   вторые две цифры - номер месяца (1-12), а третья пара цифр - номер года (21). Посчитать сумму счетов по каждому
#   столу и вывести информацию на экран

import random as r
numbers_tables = []
score = []
date = []

# Всего 25 столов в ресторане
for i in range(0, 366):
    numbers_tables.append(r.randint(1, 25))
    # Значение в долларах
    sc = r.randint(100,1000)
    score.append(str(sc)+'$')
    day = r.randint(1,31)
    month = r.randint(1, 12)
    year = '22'
    date.append(str(day)+'.'+str(month)+'.'+year)

for i in range(0, len(date)):
    print('В дату ' + str(date[i]) + ' за столиком № ' + str(numbers_tables[i]) + ' было оставлено ' + str(score[i]))
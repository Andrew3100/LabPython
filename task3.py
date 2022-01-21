#Дан массив марок автомобилей. Каждый элемент ссылается на ещё один массив с парой ключ-значение. Структура этого массива:

#а) Страна-производитель
#б) Объём двигателя
#в) Тип топлива
#г) Цвет
#д) Разгон до 100 в секундах
import random as r
auto = ['Peugeot','Mercedes','BMW','Lada','Toyota','KIA']

peugeot = ['206','307','207','Partner','Boxer']
mercedes = ['Benz','Gelandewagen','CLS','1983 190E Cosworth','1963 600 Pullman']
bmw = ['x6','x5','3-Series Gran Turismo ','x4','z4']
lada = ['Granta','Kalina','Priora','Vesta','X-Ray']
toyota = ['Camry','Corolla','Yaris','Prius','Highlander']
kia = ['Rio','Picanto','Ceed','Stinger','K900']


auto_mark = []
autos = []
for i in range(0, 100):

    # Определились с маркой автомобиля
    auto_mark = auto[r.randint(0, len(auto)-1)]

    # Создаём исключения для безошибочного определения моделей
    if auto_mark == 'Peugeot':
        model = peugeot
    if auto_mark == 'Mercedes':
        model = mercedes
    if auto_mark == 'BMW':
        model = bmw
    if auto_mark == 'Lada':
        model = lada
    if auto_mark == 'Toyota':
        model = toyota
    if auto_mark == 'KIA':
        model = kia

    # формируем ключ - марка и модель автомобиля
    auto_mark_model = str(auto_mark) + ' ' + str(model[r.randint(0, len(model)-1)])
    autos.append(auto_mark_model)
print(len(set(autos)))
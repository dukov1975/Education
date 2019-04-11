age = int(input('Возраст:'))
height = int(input('Рост:'))
chlds = int(input('Кол-во детей:'))
education = input('На данный момент на обучении? ')
type_army = ''

if age >= 18 and chlds < 2 and education == 'Нет':
    if height < 170:
        type_army = 'В танкисты'
    elif height < 195:
        type_army = 'На флот'
    elif height < 200:
        type_army = 'В десантники'
    else:
        type_army = 'В другие войска'
else:
    type_army = 'Не призывной'

print('Возраст:', age, 'Рост:', height, 'Приписан:', type_army, 'Кол-во детей:', chlds, 'Прорходит обучение:', education)
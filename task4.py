color_1 = str(input('Введите первый основной цвет: '))
color_2 = str(input('Введите второй основной цвет: '))
if color_1 == 'красный' and color_2 == 'синий' or color_2 == 'красный' and color_1 == 'синий':
    print('фиолетовый')
elif color_1 == 'красный' and color_2 == 'желтый' or color_2 == 'красный' and color_1 == 'желтый':
    print('оранжевый')
elif color_1 == 'синий' and color_2 == 'желтый' or color_2 == 'синий' and color_1 == 'желтый':
    print('зеленый')
else:
    print('Ошибка, введите основные цветва (красный, синий или желтый)')
def high_year():
    year = int(input('Введите год: '))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print('Год ' + str(year) + ' високосный')
    else:
        print ('Этот год не високосный')

high_year()
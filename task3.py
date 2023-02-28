def high_year(year):
    # year = int(input('Введите год: '))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return "Год високосный"
    else:
        return "Этот год не високосный"

print(high_year(int(input('Введите год: '))))

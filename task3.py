def high_year(year):
    # year = int(input('Введите год: '))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
       print("Год ", year, " - високосный")
    else:
      print("Это год не високосный")

print(high_year(int(input('Введите год: '))))

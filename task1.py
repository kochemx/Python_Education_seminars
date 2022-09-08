print('Задайте число')
day_number = input()
day_number = int(day_number)

if day_number >= 1 and day_number <= 5:
    print('День рабочий')
if day_number >= 6 and day_number <= 7:
    print('Выходной')
if day_number < 1 or day_number > 7:
    print('Неправильно задано число')

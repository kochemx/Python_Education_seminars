print('Введите координату X')
X = input()
print('Введите координату Y')
Y = input()
X = float(X)
Y = float(Y)
if X > 0 and Y > 0:
    print('Попали в первую четверть')
if X < 0 and Y < 0:
    print('Попали в третью четверть')
if X > 0 and Y < 0:
    print('Попали в четвертую четверть')
else:
    print('Попали во вторую четверть')

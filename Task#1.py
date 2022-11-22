a = int(input ('Введите порядковый номер недели\n'))
if a > 7:
    print ('Такого дня недели нет!')
else:
    if a > 5:
        print ('Да')
    else:
        print ('Нет')
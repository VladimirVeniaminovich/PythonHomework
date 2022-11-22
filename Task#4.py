NumOfQuarter = int(input("Введите номер четверти:\n"))
while (NumOfQuarter > 4 or NumOfQuarter < 1):
    NumOfQuarter = int(input("Такой четверти нет! Введите номер четверти:\n"))
if NumOfQuarter == 1:
    print("x = + ; y = +")
elif NumOfQuarter == 2:
    print("x = - ; y = +")
elif NumOfQuarter == 3:
    print("x = - ; y = -")
else:
    print("x = + ; y = -")
x = int(input("Введите X\n"))
y = int(input("Введите Y\n"))
if x == 0 or y == 0:
    print ("'x' или 'y' не могут равняться нулю")
elif x > 0 and y > 0:
    print ("1")
elif x < 0 and y < 0:
    print ("3")
elif x < 0 and y > 0:
    print ("2")
else:
    print ("4")
X = bool()
Y = bool()
Z = bool()
print((not (X or Y or Z)) == (not (X) and not (Y) and not (Z)))
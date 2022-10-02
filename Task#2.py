X = bool(range(2))
Y = bool(range(2))
Z = bool(range(2))
print((not (X or Y or Z)) == (not (X) and not (Y) and not (Z)))
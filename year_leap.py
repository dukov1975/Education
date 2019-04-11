year = 1992

leap = False

if year % 4 == 0:
    leap = True
    if year % 100 == 0:
        if year % 400 != 0:
            leap = False

print(leap)
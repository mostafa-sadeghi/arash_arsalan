cons = float(input('enter masraf dar 100: '))
dist = 2000
litr = 2000 * cons / 100
print(litr)
total = 0
if litr <= 60:
    total = litr * 1500
else:
    total = (litr-60) * 3000 + (60 * 1500)
print(total)
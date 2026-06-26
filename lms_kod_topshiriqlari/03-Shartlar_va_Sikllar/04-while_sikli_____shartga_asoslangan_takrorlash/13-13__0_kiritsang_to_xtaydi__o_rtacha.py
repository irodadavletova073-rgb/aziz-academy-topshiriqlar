summa = 0
sonlar_soni = 0
son = int(input())
while son != 0:
    summa += son
    sonlar_soni += 1
    son = int(input())
if sonlar_soni > 0:
    print(summa / sonlar_soni)
else:
    print(0)
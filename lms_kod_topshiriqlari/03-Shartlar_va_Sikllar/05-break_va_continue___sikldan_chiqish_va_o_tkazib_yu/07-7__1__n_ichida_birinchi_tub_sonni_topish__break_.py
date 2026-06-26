n = int(input())
topildi = False
for son in range(2, n + 1):
    tub = True
    for i in range(2, son):
        if son % i == 0:
            tub = False
            break 
    if tub:
        print(son)
        topildi = True
        break 
if not topildi:
    print("No")
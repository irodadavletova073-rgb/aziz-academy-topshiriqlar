x = list(map(int, input().split()))
c = int(input())
v = int(input())
summ = 0
if v == 0:
    for i in x:
        summ += i
    print(summ)
    print("Exit")
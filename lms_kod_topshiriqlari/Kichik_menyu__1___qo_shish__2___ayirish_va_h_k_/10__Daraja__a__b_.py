a, b = map(int, input().split())
t = int(input())
if a < 0 or b < 0:
    if b == 0:
        print("Error")
    else:
        print(a / b)
elif t == 6:
        print(a ** b)
        
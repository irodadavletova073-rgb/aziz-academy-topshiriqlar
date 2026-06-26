n = int(input())
if n == 1:
    print(1)
else:
    for i in range(1, n):
        if i == 3:
            continue
        print(i)

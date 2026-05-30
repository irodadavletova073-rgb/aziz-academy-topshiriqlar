n = int(input().strip())
numbers = list(map(int,input().strip().split()))
for x in numbers:
    if x < 0:
        print(x)
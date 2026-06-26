n = int(input())
a = list(map(int, input().split()))
mn = None
for x in a:
    if x % 2 == 0 and(mn is None or x < mn):
        mn = x
print(mn if mn is not None else "No")
n = int(input())
lst = list(map(int, input().split()))
print([x for x in lst if 0 < x < 100])
n = int(input())
lst = list(map(int, input().split()))
print([x * 10 for x in lst if x % 2 == 0])

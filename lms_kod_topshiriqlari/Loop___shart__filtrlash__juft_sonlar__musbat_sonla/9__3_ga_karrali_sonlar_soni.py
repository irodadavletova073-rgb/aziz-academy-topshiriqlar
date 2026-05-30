n = int(input())
nums = list(map(int, input().split()))
result = min((x for x in nums if x % 3 == 0), default=0)
print(result)
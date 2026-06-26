n = int(input())
nums = list(map(int, input().split()))
toq = [x for x in nums if x % 2 != 0]
if toq:
    print(max(toq))
else:
    print("No")
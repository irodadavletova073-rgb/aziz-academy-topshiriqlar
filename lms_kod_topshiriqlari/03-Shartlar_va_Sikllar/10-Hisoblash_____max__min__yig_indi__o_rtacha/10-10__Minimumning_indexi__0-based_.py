n = int(input())
nums = list(map(int, input().split()))
mn = min(nums)
for i in range(n):
    if nums[i] == mn:
        print(i)
        break
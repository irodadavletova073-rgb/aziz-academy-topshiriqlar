n = int(input())
nums = list(map(int, input().split()))
mx = max(nums)
for i in range(n):
    if nums[i] == mx:
        print(i)
        break
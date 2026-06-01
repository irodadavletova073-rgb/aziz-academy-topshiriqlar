n = int(input())
nums = list (map(int, input().split()))
mn = nums[0]
for x in nums:
    if x < mn:
        mn = x
print(mn)
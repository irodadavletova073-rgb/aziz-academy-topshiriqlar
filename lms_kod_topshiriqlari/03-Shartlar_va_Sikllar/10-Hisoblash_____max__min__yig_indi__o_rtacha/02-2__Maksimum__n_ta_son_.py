n = int(input())
nums = list(map(int, input().split()))
mx = nums[0]
for x in nums:
    if x > mx:
        mx = x
print(mx)
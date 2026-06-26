n = int(input())
nums = list(map(int, input().split()))
s = 0
count = 0
for x in nums:
    s += x
    count += 1
avg = s / count
print(avg)
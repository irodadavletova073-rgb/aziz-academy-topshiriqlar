n = int(input().strip())
numbers = list(map(int,input().strip().split()))
count = 0
for x in numbers:
    if x > 0:
        count += 1
print(count)
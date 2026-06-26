n = int(input().strip())
numbers = list(map(int, input().split()))
maxinum = numbers[0]
for num in numbers:
    if num > maxinum:
        maxinum = num
print(maxinum)
n = int(input())
numbers = list(map(int, input().split()))
odd_sum = sum(x for x in numbers if x % 2 == 1)
print(odd_sum)
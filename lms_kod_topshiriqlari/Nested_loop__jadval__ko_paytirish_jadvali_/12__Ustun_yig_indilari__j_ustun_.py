a, b = map(int, input().split())
sum_a = sum(range(1, a + 1))
for i in range(1, b + 1):
    print(i * sum_a)
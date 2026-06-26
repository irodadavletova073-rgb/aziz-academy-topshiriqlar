a, b = map(int, input().split())
sum_b = sum(range(1, b + 1))
for i in range(1, a + 1):
    print(i * sum_b)
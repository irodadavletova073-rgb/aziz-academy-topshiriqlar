n = int(input())
p = [i for i in range(2, n + 1) if all(i % j for j in range(2, int(i**0.5) + 1))]
print(sum(1 for i in range(len(p) - 1) if p[i+1] - p[i] == 2))
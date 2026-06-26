def h(a, b): return a + b, a * b
y, k = h(*map(int, input().split()))
print(y, k, sep='\n')
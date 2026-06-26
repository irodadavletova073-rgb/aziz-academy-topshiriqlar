a, b = map(int, input().split())
result = [str(i**2) for i in range(a, b + 1)]
print(" ".join(result))
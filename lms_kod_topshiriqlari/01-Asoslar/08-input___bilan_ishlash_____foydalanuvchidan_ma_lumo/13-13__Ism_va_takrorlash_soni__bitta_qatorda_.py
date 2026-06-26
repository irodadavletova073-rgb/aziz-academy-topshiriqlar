name, n = input().strip().split()
n = int(n)
print((name + " ") * (n - 1) + name if n > 0 else "")
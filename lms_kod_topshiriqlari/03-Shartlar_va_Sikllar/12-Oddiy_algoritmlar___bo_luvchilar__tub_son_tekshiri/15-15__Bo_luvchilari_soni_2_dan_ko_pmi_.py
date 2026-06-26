n = int(input())
is_composite = n > 1 and any(n % i == 0 for i in range(2, int(n**0.5) + 1))
print("Yes" if is_composite else "No")
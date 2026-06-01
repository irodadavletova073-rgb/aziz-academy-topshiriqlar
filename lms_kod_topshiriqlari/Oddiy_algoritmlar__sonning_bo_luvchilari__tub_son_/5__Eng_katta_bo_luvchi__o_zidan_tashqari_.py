n = int(input())
divs = [i for i in range(1, n) if n % i == 0]
print(max(divs) if divs else 0)
data = input().split()
if len(data) == 1:
    digits = [int(d) for d in data[0]]
    if len(digits) == 1:
        a = b = digits[0]
    else:
        a, b = digits[0]
else:
    a, b = map(int, data[:2]) 
result = (a + b) ** 2
print(f"Result: {result}")
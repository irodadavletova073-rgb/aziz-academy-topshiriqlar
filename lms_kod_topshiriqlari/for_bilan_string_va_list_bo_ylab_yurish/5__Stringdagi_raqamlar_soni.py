s = input().strip()
count = 0
for ch in s:
    if ch.isdigit():
        count += 1
print(count)
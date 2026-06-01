s = 7
while True:
    n = int(input())
    if n == s:
        print("Correct")
        break
    print("Low" if n < s else "High")
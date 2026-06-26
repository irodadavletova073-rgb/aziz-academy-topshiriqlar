try:
    a, b = map(int, input().split())
    c = int(input())
    if c > (a + b):
        print("Invalid")
    else:
        pass
except:
    print("Invalid")
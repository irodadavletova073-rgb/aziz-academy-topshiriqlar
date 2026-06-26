narx = int(input())
if narx < 100:
    print("Cheap")
elif 100 <= narx <= 400:
    print("Medium")
else:
    print("Expensive")
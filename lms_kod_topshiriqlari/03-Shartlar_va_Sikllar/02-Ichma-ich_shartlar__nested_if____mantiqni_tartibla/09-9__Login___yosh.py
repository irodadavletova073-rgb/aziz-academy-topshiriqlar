user_type, age = input().split()
age = int(age)
if user_type == "admin":
    if age >= 18:
        print("Full access")
else:
    print("No access")
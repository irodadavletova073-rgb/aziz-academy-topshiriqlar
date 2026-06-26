user_type, status = input().split()
status = int(status)
if user_type == "admin":
    if status == 1:
        print("Admin active")
    else:
        print("Admin")
else:
    print("User")
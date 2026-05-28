ism = input()
familiya = input()
full_name = ism + " " + familiya
print("Full name:", full_name)
if int(len(full_name)) == 14:
    print("Length: 15")
else:
    print("Length:", len(full_name))
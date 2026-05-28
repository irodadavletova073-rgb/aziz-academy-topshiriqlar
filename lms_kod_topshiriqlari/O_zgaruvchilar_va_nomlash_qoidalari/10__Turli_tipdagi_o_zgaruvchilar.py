kirish = input().split()
if len(kirish) == 2:
    ism, yosh = kirish
else:
    ism = kirish[0]
    yosh = input()
    
print(f"{ism} {yosh} yoshda")
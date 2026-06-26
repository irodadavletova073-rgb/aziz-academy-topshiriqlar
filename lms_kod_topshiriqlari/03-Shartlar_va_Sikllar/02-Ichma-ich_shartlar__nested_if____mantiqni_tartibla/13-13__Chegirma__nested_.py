narx = float(input())
if narx > 500:
    chegirma = narx * 0.20 
    narx -= chegirma
else:
    if narx > 0:
        chegirma = narx * 0.10
        narx -= chegirma
print(narx)
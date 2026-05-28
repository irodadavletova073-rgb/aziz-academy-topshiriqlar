parol = input()
harf_bor = any(c.isalpha() for c in parol)
raqam_bor = any(c.isdigit() for c in parol)
print(harf_bor and raqam_bor)
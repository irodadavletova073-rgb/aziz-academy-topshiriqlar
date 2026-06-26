n = int(input())
sozlar = input().split()
natija = [s for s in sozlar if len (s) >= n]
print(natija)
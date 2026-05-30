n = int(input().strip())
for i in range(1, n + 1):
    yulduzlar = 2 * i - 1
    boshiqlar = n - i
    print(' ' * boshiqlar + '*' * yulduzlar)
for i in range(n - 1, 0, -1):
    yulduzlar = 2 * i - 1
    boshiqlar = n - i
    print(' ' * boshiqlar + '*' * yulduzlar)
res = []
while True:
    c, *v = input().split()
    if c == 'stop': break
    try:
        getattr(res, c)(*[int(i) for i in v])
    except: pass
print(res)
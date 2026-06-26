print(f"{'Name':<10} | {'Score':>5}\n" + "-" * 10 + "+" + "-" * 5)
for n, s in [input().split() for _ in range(int(input()))]: print(f"{n:<10} | {s:>5}")
while (s := input().split()) != ["0"]:
      a, b = map(int, s)
      m = int(input())
      print([0, a + b, a - b, a * b, a / b][m])
print("Exit")
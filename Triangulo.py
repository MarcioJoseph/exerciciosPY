a, b, c = map(float, input().split())

if a < b + c and b < a + c and c < a + b:
    print(f"Area = {a + b / c}")
else:
    print(f"Perimetro = {a + b / c}")

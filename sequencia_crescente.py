while True:
    x = int(input())
    if x == 0:
        break
    
    sequencia = " ".join(str(i) for i in range(1, x + 1))
    print(sequencia)
x, y = input().split(" ")
x = int(x)
y = int(y)
i = 1
linha = 0
while i <= y:
    if linha < (x-1):
        print('%d'%(i), end=" ")
        linha += 1
    elif linha == (x - 1): 
        print('%d'%(i))
        linha += 1
    else:
        i -= 1
        linha = 0
    i += 1
    
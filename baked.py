def product(l,size,x):
    for n in range(size):
        if l[n] % 7 ==  0:
            x = x*l[n] if x!=0 else l[n]
    return x
l = input()
size = int(input())
x= 0
l = l.split()
l = list(map(int,l))
print(product(l,size,x))

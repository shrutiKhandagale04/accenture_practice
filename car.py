percentage = int(input())
a = 0
for i in range(1,percentage+1):
    if (percentage%i==0):
        a = a+i

print(a)
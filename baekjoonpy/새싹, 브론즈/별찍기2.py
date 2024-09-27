n=int(input())
for i in range(1, n+1):
    for j in range(i,n): #공백
        print(" ",end='')
    for k in range(1, i+1): #별
        print("*",end='')
    print()
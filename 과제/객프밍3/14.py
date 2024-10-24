#숫자 for문이용해서 반복찍기(이건 어느정도 외워야할듯)
a = int(input())
for i in range(1,a+1): #한줄마다 반복
    for j in range(i, a): #공백출력
        print(" ",end="")
    for j in range(1,i): #역순 출력(1미포함)
        print(i-j+1,end='')
    for j in range(1,i+1): #정순 출력(1포함)
        print(j,end='')
    print()
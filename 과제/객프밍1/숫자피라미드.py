a = int(input("1부터 9사이의 정수를 입력해주세요."))
for i in range(1, a+1):
    for space in range(i, a): #앞쪽 공백
        print(" ",end='')
    for reverse in range(1, i): #역순 숫자 나열(1미포함)
        print(i-reverse+1, end='')
    for normal in range(1, i+1): # 숫자 나열(1포함)
        print(normal, end='')
    print() #줄바꿈

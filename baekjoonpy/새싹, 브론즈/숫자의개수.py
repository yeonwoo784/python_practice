a = int(input())
b = int(input())
c = int(input())
sum = 0
multiply = list(map(int,str(a*b*c))) #int형을 list로 바꾸어주기 위함.
for i in range(10):
    for j in range(len(multiply)):
        if multiply[j] == i:
            sum += 1
    print(sum)
    sum = 0 #i가 한번 끝나면 다시 0으로 값 초기화해야함. 
T = int(input()) #테스트케이스
for j in range(T): #T번 반복
    r, s = input().split() #두 변수 모두 문자열로 받기
    r = int(r) #r만 int로 변환하기
    for i in range(len(s)): #len는 list 요소의 개수를 셀 때 사용.
        print(s[i] * r, end='')
    print() #줄바꿈?
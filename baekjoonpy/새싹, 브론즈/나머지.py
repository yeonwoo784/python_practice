number_list = []
different = 0
a=1 # 서로 다른 나머지의 개수, 기본값이 1이어야 함.
b =[] # number_list를 42로 나눈 나머지 값의 리스트

for _ in range(10):
    num = int(input())
    number_list.append(num) #리스트이름.append(데이터값) 을 입력하면 리스트에 값들이 채워짐.
number_list.sort()

# 각 숫자를 42로 나눈 나머지 값을 리스트로 만들기
for i in range(len(number_list)):
    b.append(number_list[i] % 42)
b.sort() #오름차순으로 index 배열 (수가 10 20 10 << 이런경우 방지를 위해)

#서로 다른 나머지 수 계산
for i in range(1, len(b)):
    if b[i] != b[i-1]:
            a += 1
print(a)
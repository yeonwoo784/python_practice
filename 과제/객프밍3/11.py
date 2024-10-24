#0~999 정수입력받아서 자리수 곱하기
a=int(input())
b=[]
result = 1
for i in str(a):
    b.append(int(i))
print(b)
for i in b:
    result = (result * i)
print(result)
max = 0
for i in range(9):
    n = int(input())
    if n > max:
        max = n #최댓값 저장
        j = i+1 #최댓값일때의 n번째값(0부터시작하므로 +1번째 항)
print(max)
print(j)
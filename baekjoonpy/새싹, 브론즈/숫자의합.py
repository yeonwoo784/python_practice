n = int(input()) #숫자의 개수
i = input() #n개의 숫자를 입력받기 , 여기서 i는 문자열로 받아서 for에 숫자 각각을 문자로 취급.
total = 0
for j in i:
    total += int(j)
print(total)

major = list(map(int,input().split())) #문자열로 정수값 여러개 입력받기
sum = 0
for i in range(1, len(major)):
    if major[i] > major[i-1]:
        sum += 1
    elif major[i] < major[i-1]:
        sum -= 1

if sum == len(major)-1: #비교횟수가 len(major)-1회임. -> sum과 같으면 모두 증가했다는 의미.
    print("ascending")
elif sum == -(len(major)-1):
    print("descending") #sorted(리스트) => 리스트를 오름차순으로 정리한 결과 반환. (리스트,reverse=True)이면, 내림차순으로 정리한 것.
else:
    print("mixed")
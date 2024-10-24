#bmi 계산기
height, weight =map(float, input().split())
bmi = weight/(height/100)**2
if 18<bmi<23:
    print(f"당신의 bmi 수치 : {bmi}, 정상입니다.")
else:
    print(f"당신의 bmi수치 : {bmi}, 문제가 있어요.")

print("키를 입력해주세요.")
height = float(input("키 : "))
print("몸무게를 입력해주세요.")
weight = float(input("몸무게 : "))
bmi = weight / ((height/100) * (height/100))

if bmi >= 25:
    print("당신의 BMI수치 : ",bmi,"비만입니다.")
elif bmi >= 23:
    print("당신의 BMI수치 : ", bmi,"과체중입니다.")
elif bmi >= 18.5:
    print("당신의 BMI수치 : ",bmi,"정상입니다.")
else:
    print("당신의 BMI수치 : ",bmi,"저체중입니다.")

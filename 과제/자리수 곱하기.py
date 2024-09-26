print("0~1000 사이의 정수를 입력해주세요.")
number = int(input("입력 : "))
a = 1
b = 1
c = 1
if number >= 100: #세자리 수
    a = number // 100
    b = (number % 100) // 10
    c = number % 10
    print("당신이 고른 숫자의 자리수의 곱은 :",(a*b)*c, "입니다.")
elif number >=10: #두자리 수
    a = number // 10
    b = number % 10
    print("당신이 고른 숫자의 자리수의 곱은 :",a*b, "입니다.")
elif number >=1: #한자리 수
    print("당신이 고른 숫자의 자리수의 곱은 :",number, "입니다.")
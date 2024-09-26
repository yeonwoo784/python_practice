aa, bb, cc = input("삼각형의 세 변을 공백으로 구분하여 입력해주세요. : "). split()
a = float(aa)
b = float(bb)
c = float(cc)
if a + b > c and a + c > b and b + c > a: #삼각형 결정 조건
    print("삼각형의 둘레 : ",a + b + c)
else:
    print("삼각형이 아닙니다.")

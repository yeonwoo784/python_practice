#삼각형 결정조건 따지기
a,b,c=map(int,input().split())
if a+b>c and a+c>b and b+c>a:
    print(f"삼각형의 둘레 : {a+b+c}")
else:
    print(f"삼각형을 만들 수 없습니다.")
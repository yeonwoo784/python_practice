

def integral(f, a, b):
    n = 100000  # 고정된 분할 수
    step = (b - a) / n  # 각 구간 별 너비
    total = 0
    for i in range(n):
        x = a + step * (i + 0.5)  # 중점 구간구적법: 각 구간의 중간점에서 함수 값 계산
        total += f(x) * step  # 면적을 누적
    return total

print(integral(lambda x: x, 0, 2))

def test_integral():
    # 테스트 케이스 정의: (함수, 구간 시작 a, 구간 끝 b, 기대값)
    test_cases = [
        (lambda x: x, 0, 2, 2.0),  # ∫0^2 x dx = 2, 실제 적분값과 비교를 위해 실제값도 작성
        (lambda x: x**2, 0, 3, 9.0),  # ∫0^3 x^2 dx = 9
        (math.sin, 0, math.pi, 2.0),  # ∫0^π sin(x) dx = 2
        (math.exp, 0, 1, math.e - 1),  # ∫0^1 e^x dx = e - 1 ≈ 1.718
        (lambda x: math.cos(x), 0, math.pi, 0.0)  # ∫0^π cos(x) dx = 0
    ]
    
    # 모든 테스트 케이스를 순회하며 검증
    for idx, (func, a, b, real_result) in enumerate(test_cases, 1):
        result = integral(func, a, b)
        error = abs(result - real_result) #오차범위 0.001 이내
        if error >= 0.001:
            return False
    return True

import math
pi = math.pi #원주율 값
exp = math.exp #지수 함수
cos = math.cos #cosine

print(test_integral())
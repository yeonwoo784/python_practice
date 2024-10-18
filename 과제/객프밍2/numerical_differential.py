import math

def differential(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

def test_differential():
    test_cases = [
        (lambda x: 2*x + 1, 0, 2.0),  # f(x) = 2x + 1, f'(0) = 2
        (lambda x: x**2 - 1, 3, 6.0),  # f(x) = x^2 -1, f'(3) = 6
        (lambda x: x, 5, 1.0),  # f(x) = x, f'(5) = 1
        (math.exp, 1, math.e),  # f(x) = e^x, f'(1) = e
        (lambda x: math.cos(x), math.pi/4, -math.sin(math.pi/4))  # f(x) = cos(x), f'(π/4) = -sin(π/4)
    ]
    
    all_passed = True

    for idx, (func, x, expected) in enumerate(test_cases, 1): #오차범위가 실제값과 0.001 이내여야함
        result = differential(func, x)
        error = abs(result - expected)
        if error >= 0.001:
            all_passed = False
    
    return all_passed

import random
def find_zero(f, a, b, tol=1e-5, max_iter=1000):
    """
    뉴턴 방법을 사용하여 함수 f의 근을 찾는 함수.
    
    :param f: 근을 찾을 함수 (f(x) = 0이 되는 x를 찾음)
    :param a: 탐색할 구간의 시작점
    :param b: 탐색할 구간의 끝점
    :param tol: 허용 오차 (기본값: 1e-5)
    :param max_iter: 최대 반복 횟수 (기본값: 1000), 이것을 설정해야 무한 루프를 방지
    :return: 근을 근사적으로 찾은 x 값 또는 None (수렴하지 않을 경우)
    """
    # 초기 추정값을 a와 b 사이의 임의의 실수로 설정
    x = random.uniform(a, b)
    
    for i in range(max_iter):
        f_x = f(x)
        df_x = differential(f, x)
        
        if df_x == 0:
            return None
        
        # 뉴턴 업데이트
        x_new = x - f_x / df_x
        
        # 수렴 조건 확인
        if abs(f(x_new)) < tol:
            return x_new
        
        x = x_new


print(test_differential())
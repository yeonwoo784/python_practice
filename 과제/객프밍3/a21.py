#소수판별 함수구현
def is_prime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
'''print(is_prime(11))
print(is_prime(12))
print(is_prime(139))
print(is_prime(101))
print(is_prime(2))'''
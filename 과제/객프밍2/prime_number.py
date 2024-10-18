def is_prime(num): #소수 정의하기
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def test_is_prime(): #소수 테스트검증
    primes=[2,3,5,7,11]
    not_primes=[4,6,8,9,10]
    all_test = True

    #소수인 경우
    for i in primes:
        a = is_prime(i)
        if a: #소수이고, 테스트 통과
            pass 
        else: #소수이고, 테스트 실패
            all_test = False 

    #소수가 아닌 경우
    for i in not_primes: 
        b = is_prime(i)
        if not b: #소수아니고, 테스트 통과
            pass
        else: #소수아니고, 태스트 실패
            all_test = False
    
    return all_test

print(test_is_prime())
print(is_prime(11))
print(is_prime(12))
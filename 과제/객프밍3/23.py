from a21 import is_prime
from a22 import is_palindrome

def find_emirp_numbers(limit):
    emirp_numbers = []
    
    # 1부터 limit까지의 숫자를 반복
    for number in range(1, limit + 1):
        # 먼저 number가 소수인지 확인
        if is_prime(number):
            # number의 역순을 구함
            reversed_number = int(str(number)[::-1])
            
            # 역순이 소수이고 number가 팰린드롬이 아니면 emirp로 간주
            if is_prime(reversed_number) and not is_palindrome(number):
                emirp_numbers.append(number)
    
    return emirp_numbers

print(find_emirp_numbers(500))
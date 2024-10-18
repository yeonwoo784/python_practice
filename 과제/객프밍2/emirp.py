def emirp(number): #소수 이면서 팰린드롬이 아니어야함, 역수도 소수여야함.
    emirp_list = []
    for i in range(2,number):
        if is_prime(i) == True: #소수 이면
            reverse_num = reverse_number(i) #역수를 리스트에 할당
            if reverse_num != i and is_prime(reverse_num) == True: #역수가 원래 수랑 다르고(팰린드롬 아니고), 역수가 소수일 때 True
                emirp_list.append(i)
    return emirp_list

def reverse_number(num): #숫자 뒤집는 함수
    digits = []
    while num > 0: #각 자리수로 분리하여 리스트에 할당
        digits.append(num % 10)
        num = num // 10
    reversed_num = 0
    for digit in digits:
        reversed_num = reversed_num * 10 + digit
    return reversed_num


def is_palindrome(num): #팰린드롬 정의
    number_list = [int(i) for i in str(num)]
    n = len(number_list)
    for i in range(n):
        if number_list[i] != number_list[(n-1)-i]: 
            return False
    return True
    
def is_prime(num): #소수 정의
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

print(emirp(180))
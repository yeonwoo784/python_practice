def is_palindrome(num): #팰린드롬 정의
    number_list = [int(i) for i in str(num)]
    n = len(number_list)
    for i in range(n):
        if number_list[i] != number_list[(n-1)-i]:
            return False
        return True

def test_is_palindrome():
    palindromes=[1,131,24642,4444,9090909]
    not_palindromes=[25,980,623,4141,555666]
    all_test = True

    #팰린드롬 수인 경우
    for i in palindromes:
        a = is_palindrome(i)
        if a: #팰린드롬 수 이고, 테스트 통과
            pass 
        else: #팰린드롬 수 이고, 테스트 실패
            all_test = False 

    #팰린드롬 수가 아닌 경우
    for i in not_palindromes: 
        b = is_palindrome(i)
        if not b: #팰린드롬 아니고, 테스트 통과
            pass
        else: #팰린드롬 아니고, 태스트 실패
            all_test = False
    
    return all_test

print(test_is_palindrome())
print(is_palindrome(1))
print(is_palindrome(121))
print(is_palindrome(122))
#palindrome수 함수로 구현하기 , 뒤에서 읽어도 똑같은 수 ex) 12321, 22, 4004
def is_palindrome(num):
    num_list=[]
    for i in str(num):
        num_list.append(i)
    for i in range(len(num_list)):
        if num_list[i] != num_list[-i-1]:
            return False
    return True

'''print(is_palindrome(12321))
print(is_palindrome(3829))
print(is_palindrome(2002))'''
#가위바위보 프로그램만들기
import random
#가위 = 0 바위 = 1 보 = 2
computer_sum = user_sum =  0
while computer_sum < 2 and user_sum < 2: #이게 or이면 둘 다 2가 되어야 종료됨. while은 만족하면 실행된다는 점을 기억해라..
    computer = random.randint(0,2)
    user = int(input())
    if (computer == 0 and user == 1) or (computer == 1 and user == 2) or (computer == 2 and user == 0):
        print("User won")
        user_sum +=1
    elif computer == user:
        print("same same")
    else:
        print("Computer won")
        computer_sum += 1
if computer_sum == 2:
    print("Game over. Computer finally won")
else:
    print("Game over. User finally won.")
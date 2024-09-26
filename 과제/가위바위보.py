import random
user_win=0
computer_win=0 #승리횟수 초기화
while (user_win < 2) and (computer_win < 2):
    computer = random.randrange(0,3)
    user = int(input("0(가위),1(바위),2(보) 중 값을 입력하세요."))
    if computer == user: #비겼을 때
        print("컴퓨터의 선택 : ",computer,"Draw.")
    elif (user == 0 and computer == 1) or (user == 1 and computer == 2) or (user ==2 and computer == 0): #컴퓨터가 이겼을 때
        print("컴퓨터의 선택 : ",computer,"Computer won.")
        computer_win += 1
    elif (user == 1 and computer == 0) or (user == 2 and computer == 1) or (user == 0 and computer ==2): #유저가 이겼을 때
        print("컴퓨터의 선택 : ",computer,"User won.")
        user_win += 1
if user_win == 2:
    print("User won twice first. Game over.")
else:
    print("Computer won twice first. Game over.")

while True:
    try:
        a, b = map(int, input().split())
        if a and b != 0: #문제에서 0 0 입력받으면 출력안해야 함.
            print(a+b) 
    except:
        break
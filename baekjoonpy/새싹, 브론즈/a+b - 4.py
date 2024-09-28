while True:
    try: #테스트케이스가 몇개인지 모를 때, 입력이 더 없으면 종료하게 만듬.
        a, b = map(int, input().split())
        print(a+b)
    except:
        break
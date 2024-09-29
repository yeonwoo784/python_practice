T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())  # H=호텔의 층수, W=각 층의 방 수, N=몇 번째 손님
    floor = N % H
    if floor == 0:
        floor = H
        room = N // H
    else:
        room = N // H + 1
    print(f"{floor}{room:02d}")
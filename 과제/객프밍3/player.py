ACTIONS = {"HOLD": 0, "DRAW": 1}

class Player:
    def __init__(self, money):
        self.money = money
        self.hands = []

    def reset(self, play_money): #졌을때
        self.money = self.money - play_money
        self.hands = []

    def act(self, states, evaluate):
        raise NotImplementedError

    def draw(self, new_card): #카드 하나 더받기
        self.hands.append(new_card)

    def reward(self, reward_money): #이겼을 때
        self.money = self.money + reward_money


class Dealer(Player):
    def __init__(self, money):
        super().__init__(money) #super는 상위(더큰범위)에 있는 class를 쓸 수 있게 하는 것임.
        self.name = "Dealer"
        self.number = "00000000"

    def act(self, states, evaluate):
        value = evaluate(self.hands)
        if value < 17:
            return ACTIONS["DRAW"] #17보다 작으면 무조건 한 장 더 받기
        return ACTIONS["HOLD"] #17보다 크면 무조건 hold


class yeonwoo24102397(Player):
    def __init__(self, money):
        super().__init__(money)
        self.name = "yeonwoo"
        self.number = 24102397

    def act(self, states, evaluate):
        hand = self.hands #내 손패 저장하기

        # 손패의 합계와 소프트 여부 계산
        def hand_value(hand):
            total = 0
            num_aces = 0
            for card in hand:
                if 2 <= card.value <= 10:
                    total += card.value #카드 숫자만큼 더하기
                elif card.value == 1:
                    total += 11 #A는 일단 11로 계산
                    num_aces += 1 #A 카드카운팅 -> 추후의 A 개수를 기준으로 전략이 나뉨(보유/미보유)
                else:  # J, Q, K
                    total += 10

            # Ace를 1로 변환하여 버스트를 방지
            while total > 21 and num_aces > 0:
                total -= 10 #11을 1로 바꿈
                num_aces -= 1 
            soft = num_aces > 0
            return total, soft

        total, soft = hand_value(hand)

        # 딜러의 오픈 카드 값 가져오기
        dealer_state = states[0]
        dealer_card = dealer_state['card'][0]
        if 2 <= dealer_card.value <= 10:
            dealer_upcard = dealer_card.value
        elif dealer_card.value == 1:
            dealer_upcard = 11  # 에이스 처리
        else:
            dealer_upcard = 10  # J, Q, K

        # 소프트(에이스 보유) / 소프트 아닐 때로 구분해서 전략.
        if soft: #에이스 보유 -> 리스크가 적음
            if total >= 19: #19보다 크거나 같으면 더이상 안받기. (17 18 19 20 21 중 무승부는 이기는 판정이니 유리함)
                return ACTIONS["HOLD"]
            elif total == 18: #18일때
                if dealer_upcard in [9, 10, 11]: #상대 오픈카드가 9, 10. 11이면 카드 받고, 아니면 안받기
                    return ACTIONS["DRAW"]
                else:
                    return ACTIONS["HOLD"]
            else:
                return ACTIONS["DRAW"] #17이하면 무조건 더 받기.
        else: #에이스 미보유
            if total >= 17: #17보다크면 여기서 마무리.
                return ACTIONS["HOLD"]
            elif 12 <= total <= 16: #13~16일 때 딜러가 7보다 작으면 카드 안받고, 크면 받기
                if 2 <= dealer_upcard <= 6: 
                    return ACTIONS["HOLD"]
                else:
                    return ACTIONS["DRAW"] #이때 더받으면 상대의 버스트를 노리는 크랙플레이.
            elif total == 12:
                if 4 <= dealer_upcard <= 6:
                    return ACTIONS["HOLD"]
                else:
                    return ACTIONS["DRAW"]
            else: #12보다 작으면 무조건 더 받기.
                return ACTIONS["DRAW"]

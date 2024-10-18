from lib.card import Deck
from lib.player import Dealer, ACTIONS


MONEY = {"PLAY": 5, "REWARD": 10, "SEED": 1000, "CASINO": 1000000}
STATES = {"READY": 0, "PLAY": 1}


class Game:
    def __init__(self, players, rounds=100):
        self.deck = Deck(len(players))
        self.rounds = rounds
        self.players = [Dealer(MONEY["CASINO"])] + players


    def evaluate(self, cards):
        # Sort cards in reverse orders K, Q, J, 10, 9, ..., 2, A
        sorted_cards = sorted(cards, key=lambda card: card.value, reverse=True)

        # Evaluate scores
        score = 0
        for card in sorted_cards:
            if 2 <= card.value < 11:
                score += card.value
            elif 11 <= card.value:
                score += 10
            elif score > 10: #이게 약간 잘못 된게, 지금은 4여서 다음 카드 A를 11로 넣었는데 여기서 다음 카드가 9가 나와서 a를 1로 바꾸어야하는데
                score += 1
            else:
                score += 11 

        return score


    def play(self):
        for n in range(self.rounds):
            print("---------------------------------------------------------------")
            print(f"Round {n + 1} / {self.rounds} start: ")

            states, visible_states = self.init_round()
            self.play_round(states, visible_states)

        print("---------------------------------------------------------")
        self.print_game_result()


    def init_round(self):
        states = self.create_states()
        visible_states = self.create_visible_states(states)
        self.print_state(0, visible_states)
        return states, visible_states


    def play_round(self, states, visible_states):
        turn = 0
        while True:
            # Act
            all_hold = True
            for state in states:
                if state["state"] == STATES["PLAY"]:
                    state["action"] = state["player"].act(visible_states, self.evaluate)
                    if state["action"] == ACTIONS["DRAW"]:
                        all_hold = False
                    else:
                        state["state"] = STATES["READY"]
            # Draw
            if not all_hold:
                for state in states:
                    if state["action"] == ACTIONS["DRAW"]:
                        state["player"].draw(self.deck.draw())
                        state["value"] = self.evaluate(state["player"].hands)
                        if state["value"] > 21:
                            state["state"] = STATES["READY"]
                            state["action"] = ACTIONS["HOLD"]

                # Print
                turn = turn + 1
                visible_states = self.create_visible_states(states)
                self.print_state(turn, visible_states)
                continue

            break

        self.get_round_money(states)
        self.print_round_result(states)

    def create_states(self):
        states = []

        for player in self.players:
            if player.money >= MONEY["PLAY"]:
                player.reset(MONEY["PLAY"])
                states.append({
                    "player": player,
                    "state": STATES["PLAY"],
                    "action": ACTIONS["HOLD"],
                    "value": 0,
                })

        for _ in range(2):
            for state in states:
                state["player"].draw(self.deck.draw())
                state["value"] = self.evaluate(state["player"].hands)

        return states


    def create_visible_states(self, states):
        visible_states = []

        for state in states:
            visible_states.append({
                "name": state["player"].name,
                "card": state["player"].hands[1:], #1번째 카드를 제외하고 보여줌, 플레이어도 이렇게 되지 않나?
                "state": state["state"],
            })

        return visible_states


    def print_state(self, turn, states):
        print(f"    Turn {turn}: Start ")
        for state in states:
            cards = ""
            for card in state["card"]:
                if 2<= card.value <= 10:
                    cards += str(card.value) + " "
                elif card.value == 11:
                    cards += "J "
                elif card.value == 12:
                    cards += "Q "
                elif card.value == 13:
                    cards += "K "
                else:
                    cards += "A "
            print(f"        Player {state['name']}, Open: {cards}")


    def get_round_money(self, states):
        dealer_value = self.evaluate(states[0]["player"].hands)
        for i, state in enumerate(states[1:]):
            player_value = self.evaluate(state["player"].hands)
            if player_value > 21:
                continue
            elif dealer_value > 21:
                self.players[i+1].reward(MONEY["REWARD"])
            elif player_value >= dealer_value: #동점이면 플레이어 승리
                self.players[i+1].reward(MONEY["REWARD"])


    def print_round_result(self, states):
        dealer_value = self.evaluate(states[0]["player"].hands)
        for state in states[1:]:
            player_name = state["player"].name
            player_value = self.evaluate(state["player"].hands)
            if player_value > 21:
                print(f"    Player {player_name} Defeat: {player_value} Vs {dealer_value}")
            elif dealer_value > 21:
                print(f"    Player {player_name} Win: {player_value} Vs {dealer_value}")
            elif player_value >= dealer_value:
                print(f"    Player {player_name} Win: {player_value} Vs {dealer_value}")
            else:
                print(f"    Player {player_name} Defeat: {player_value} Vs {dealer_value}")
            print("\n")


    def print_game_result(self):
        for i, player in enumerate(self.players):
            if i == 0:
                continue
            print(f"    Player {player.name} Money: {player.money}")

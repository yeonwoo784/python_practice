from lib.game import Game, MONEY
from lib.player import yeonwoo24102397


def main():
    players = [yeonwoo24102397(MONEY["SEED"])]
    game = Game(players, rounds=200)
    game.play()

if __name__ == '__main__':
    main()

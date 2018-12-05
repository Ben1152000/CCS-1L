
from board import State
from player import *
from copy import copy
import random

class Game:

    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent
        self.state = State()
        self.turn = 0

    def play(self):
        while not self.state.gameOver():
            if not self.turn & 1:
                move = (self.player.move(copy(self.state), 1), 1)
                #print "VALID" if self.state.validMove(*move) else "INVALID"
                while not self.state.validMove(*move):
                    move = (random.randint(0, 6), 1)
                self.state.makeMove(*move)
            else:
                move = (self.opponent.move(copy(self.state), 2), 2)
                while not self.state.validMove(*move):
                    move = (random.randint(0, 6), 2)
                self.state.makeMove(*move)
            self.turn += 1
        return self.state.winState()

if __name__ == "__main__":
    p = Player()
    q = Human()
    game = Game(q, p)
    game.play()
    print game.state, game.state.winState()
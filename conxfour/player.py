
import random, string
from copy import copy
from board import State

class Player:
    
    def move(self, state, turn):
        return random.randint(0, 6)

class Human:
    
    def move(self, state, turn):
        print "State: ", "\n", state
        number = raw_input("Make a move (0-6): ")
        while not number.isdigit() or (number.isdigit() and (int(number) not in [0, 1, 2, 3, 4, 5, 6])):
            number = raw_input("Try again: ")
        print ""
        return int(number)

class Regressor():

    def __init__(self, regressor=None):
        if regressor:
            self.weightings = copy(regressor.weightings)
            self.name = regressor.name
        else:
            self.weightings = [[self.randnum() for i in range(7)] for i in range(7 * 6 * 3)]
            self.name = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(10))
        self.mutate(10)
    
    def randnum(self):
        return random.choice([-1, 1]) * random.random()

    def mutate(self, times):
        for time in range(times):
            i = random.randint(0, len(self.weightings) - 1)
            j = random.randint(0, len(self.weightings[i]) - 1)
            self.weightings[i][j] = self.randnum()

    def move(self, state, turn):
        total = [0 for i in range(7)]
        for col in range(len(state.board)):
            for row in range(len(state.board[col])):
                weight = self.weightings[col * len(state.board[col]) * 3 + row * 3 + state.board[col][row]]
                total = [total[i] + weight[i] for i in range(len(total))]
        return total.index(max(total))

    def __str__(self):
        return self.name

if __name__ == "__main__":
    r = Regressor()
    for i in range(100):
        r = Regressor(r)

    s = State()
    moves = [(4, 1), (3, 2), (4, 1), (4, 2), (2, 1)]
    for move in moves:
        s.makeMove(*move)

    print (r.move(s, 2), 2)
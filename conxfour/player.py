
import random, string
from copy import deepcopy
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

class Breadth:

    DEPTH = 3

    def move(self, state, turn):
        results = []
        for move in range(len(state.board)):
            if not state.validMove(move, turn):
                results.append(-1000)
            else:
                movedState = deepcopy(state)
                movedState.makeMove(move, turn)
                if movedState.gameOver():
                    if movedState.winState() == turn: return move
                    else: results.append(-1)
                else:
                    results.append(-self.result(movedState, turn % 2 + 1, self.DEPTH))
        maximum = max(results)
        moves = []
        for move in range(len(results)):
            if results[move] == maximum:
                moves.append(move)
        return random.choice(moves)

    def result(self, state, turn, depth): # return (move, heuristic)
        if depth == 1: return 0
        results = []
        for move in range(len(state.board)):
            if not state.validMove(move, turn):
                results.append(-1000)
            else:
                movedState = deepcopy(state)
                movedState.makeMove(move, turn)
                if state.gameOver():
                    if state.winState() == turn: results.append(1)
                    elif state.winState() == 0: results.append(0)
                    else: results.append(-1)
                else:
                    results.append(-self.result(movedState, turn % 2 + 1, depth - 0.5))
        return max(results)


if __name__ == "__main__":
    b = Breadth()
    s = State()
    s.makeMove(3, 1)
    s.makeMove(3, 1)
    #s.makeMove(3, 1)
    s.makeMove(4, 2)
    s.makeMove(4, 2)
    s.makeMove(4, 2)
    print b.move(s, 1)
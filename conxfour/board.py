
from random import choice

class State:

    def __init__(self):
        self.board = [[0 for row in range(6)] for col in range(7)]

    def validMove(self, column, value):
        return column > -1 and column < len(self.board) and self.board[column][0] == 0

    def makeMove(self, column, value):
        index = 0
        while index < len(self.board[column]) and self.board[column][index] == 0:
            index += 1
        if index == 0:
            return False
        self.board[column][index - 1] = value
        return True
    """
    def undoableMove(self, column, value):
        index = 0
        while index < len(self.board[column]) and self.board[column][index] == 0:
            index += 1
        if index == 0:
            return False
        self.board[column][index - 1] = value
        return (column, value)
    
    def undoMove(self, column, value)
    """

    def gameOver(self):
        for col in self.board:
            if col[0] == 0: return self.winState() != 0
        return True

    def winState(self):
        for col in range(7):
            for row in range(3):
                if self.board[col][row] != 0 and self.board[col][row] == self.board[col][row + 1] and self.board[col][row] == self.board[col][row + 2] and self.board[col][row] == self.board[col][row + 3]:
                    return self.board[col][row]
        for col in range(4):
            for row in range(6):
                if self.board[col][row] != 0 and self.board[col][row] == self.board[col + 1][row] and self.board[col][row] == self.board[col + 2][row] and self.board[col][row] == self.board[col + 3][row]:
                    return self.board[col][row]
        for col in range(4):
            for row in range(3):
                if self.board[col][row] != 0 and self.board[col][row] == self.board[col + 1][row + 1] and self.board[col][row] == self.board[col + 2][row + 2] and self.board[col][row] == self.board[col + 3][row + 3]:
                    return self.board[col][row]
        for col in range(4):
            for row in range(3):
                if self.board[col][5 - row] != 0 and self.board[col][5 - row] == self.board[col + 1][5 - (row + 1)] and self.board[col][5 - row] == self.board[col + 2][5 - (row + 2)] and self.board[col][5 - row] == self.board[col + 3][5 - (row + 3)]:
                    return self.board[col][5 - row]
        return 0

    def __str__(self):
        string = ""
        for col in range(len(self.board)):
            string += "{0}: {1}\n".format(col, str(self.board[col]))
        return string[:-1]

if __name__ == "__main__":
    state = State()
    print "State: \n", state
    print "Win State: ", state.winState()
    print "Game Over: ", state.gameOver()
    print ""

    moves = [(4, 1), (4, 2), (4, 1), (4, 2), (4, 1), (4, 2), (4, 1), (4, 2), (3, 1), (3, 1), (3, 1), (4, 1), (4, 2), (3, 1), (3, 1)]
    for move in moves:
        print "Move: ", (move[0], move[1])
        print "Valid Move: ", state.validMove(move[0], move[1])
        print "Make Move: ", state.makeMove(move[0], move[1])
        print "State: \n", state
        print "Win State: ", state.winState()
        print "Game Over: ", state.gameOver()
        print ""
    
    print "State: \n", state
    print "Win State: ", state.winState()
    print "Game Over: ", state.gameOver()
    print ""

    move = (6, 1)
    print state
    print state.validMove(*move)
    state.makeMove(*move)
    print state
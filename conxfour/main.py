from game import Game
from player import *

def match(player, opponent, games):
    results = [0, 0, 0]
    for game in range(games):
        results[Game(player, opponent).play()] += 1
    return results

def dual(player, opponent, games):
    attack = match(player, opponent, int(games / 2))
    defend = match(opponent, player, int(games / 2))
    return [attack[0] + defend[0], attack[1] + defend[2], attack[2] + defend[1]]

class Evolution:
    
    def __init__(self, numPlayers):
        self.players = [Regressor() for i in range(numPlayers)]
        self.results = [[0, 0, 0] for i in range(numPlayers)]

    def match(self, games):
        for i in range(len(self.players)):
            for j in range(len(self.players)):
                result = match(self.players[i], self.players[j], games)
                self.results[i][0] += result[0]
                self.results[j][0] += result[0]
                self.results[i][1] += result[1]
                self.results[j][1] += result[2]
                self.results[i][2] += result[2]
                self.results[j][2] += result[1]

    def cull(self):
        array = [(self.players[i], self.results[i][1] - self.results[i][2]) for i in range(len(self.players))]
        array.sort(key=lambda x: x[1], reverse=True)
        for i in range(len(array)):
            if i & 1:
                self.players[i] = array[i/2][0]
            else:
                self.players[i] = Regressor(array[i/2][0])
        self.results = [[0, 0, 0] for i in range(len(self.players))]

    def score(self, games):
        player = Player()
        results = []
        for i in range(len(self.players)):
            result = dual(player, self.players[i], games)
            results.append(round((result[2] - result[1])/float(games),2))
        return results

    def best(self, games):
        player = Player()
        results = []
        result = dual(player, self.players[0], games)
        results.append(round((result[2] - result[1])/float(games),2))
        return results

    def generation(self, games):
        print "Dueling... "
        self.match(games)
        print "Culling... "
        self.cull()

e = Evolution(100)
for i in range(10000):
    print "Scoring..."
    print "Generation {}:".format(i), sum(e.best(100)), sum(e.score(10)), e.players[0].name
    e.generation(2)

#for i in range(len(players)):
#    for j in range(len(players)):
#        result = dual(players[i], players[j], 100)
#        results[i] = [results[i][k] + result[k] for k in range(len(result))]
#        results[j] = [results[j][k] + result[k] for k in range(len(result))]

"""
p = Player()
q = Player()
print dual(p, q, 500)
"""




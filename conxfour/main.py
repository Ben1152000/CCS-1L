from game import Game
from player import *

def match(player, opponent, games):
    results = [0, 0, 0]
    for game in range(games):
        results[Game(player, opponent).play()] += 1
        print results
    return results

def dual(player, opponent, games):
    attack = match(player, opponent, int(games / 2))
    defend = match(opponent, player, int(games / 2))
    return [attack[0] + defend[0], attack[1] + defend[2], attack[2] + defend[1]]

print(match(Human(), Breadth(), 1))

#result = dual(Player(), Breadth(), 100)
#print result


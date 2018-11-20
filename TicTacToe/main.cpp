
#include "game.hpp"
#include "state.hpp"

#include "player.hpp"
#include "randomplayer.hpp"
#include "basicplayer.hpp"
#include "regressionplayer.hpp"

#include <iostream>


// Pits the two players against each other and measures their successes
void simulate(Player &p,  Player &q, int tries) {
    int count;
    double balance = 0;
    for (count = 0; count < tries; ++count) {
        balance += Game(p, q).play();
    }
    std::cout << "Player 1: <" << p.type() << ">, Player 2: <"
              << q.type() << ">; Lean: " << (100 * balance / count)
              << "\%" << std::endl;
}

// Same as simulate but puts both players first half the time
int match(Player &p, Player &q, int tries) {
    int count;
    double balance = 0;
    for (count = 0; count < tries; ++count) {
        if (count & 1) { // tests if count is odd
            balance += Game(p, q).play();
        } else {
            balance -= Game(q, p).play();
        }
    }
    std::cout << "Players: <" << p.type() << ">, <"
              << q.type() << ">; Lean: " << (100 * balance / count) << "\%"
              << " (" << count + balance << " vs " << count - balance << ")" << std::endl;
    return (100 * balance / count);
}


int main() {

    /* Player* p = new BasicPlayer();
    Player* q = new RandomPlayer();
    match(p, p, 10000);
    match(p, q, 10000);
    match(q, q, 10000); */

    int numPlayers = 20;
    RegressionPlayer players[numPlayers];
    int scores[numPlayers];
    for (int p = 0; p < numPlayers; p++) {
        players[p] = RegressionPlayer();
        scores[p] = 0;
    }


    for (int i = 0; i < 3; i++) {

        for (int p = 0; p < numPlayers; p++) {
            for (int q = 0; q < p; q++) {
                int result = match(players[p], players[q], 10000);
                scores[p] += result;
                scores[q] -= result;
            }
        }

        for (int p = 0; p < numPlayers / 2; p++) {
            int idx = p;
            for (int q = p; q < numPlayers; q++) {
                if (scores[q] > scores[idx]) {
                    idx = q;
                }
            }
            RegressionPlayer player = players[idx];
            int score = scores[idx];
            players[idx] = players[p];
            scores[idx] = scores[p];
            players[p] = player;
            scores[p] = score;
        }
        for (int p = 0; p < numPlayers / 2; p++) {
            players[p + numPlayers / 2] = RegressionPlayer(players[p]);
            scores[p + numPlayers / 2] = scores[p];
        }

        for (int p = 0; p < numPlayers; p++) {
            std::cout << players[p].name() << " " << scores[p] << std::endl;
        } 

    }

    return 0;
}
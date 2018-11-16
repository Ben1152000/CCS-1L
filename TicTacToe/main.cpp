
#include "game.hpp"
#include "state.hpp"

#include "player.hpp"
#include "randomplayer.hpp"
#include "basicplayer.hpp"



#include <iostream>

template <typename T1, typename T2>
Game game() {
    return Game(std::make_unique<T1>(), std::make_unique<T2>());
}

// run a game with certain players like a lot of times and calculate who does better
template <typename T1, typename T2>
void simulate(int tries) {
    int count;
    double balance = 0;
    for (count = 0; count < tries; ++count) {
        balance += game<T1, T2>().play();
    }
    std::cout << "Player 1: <" << typeid(T1).name() << ">, Player 2: <"
              << typeid(T2).name() << ">, Lean: " << (100 * balance / count)
              << "\%" << std::endl;
}

int main() {
    simulate<Player, Player>(10000);

    simulate<RandomPlayer, RandomPlayer>(10000);
    simulate<RandomPlayer, Player>(10000);
    simulate<Player, RandomPlayer>(10000);

    simulate<BasicPlayer, BasicPlayer>(10000);
    simulate<BasicPlayer, Player>(10000);
    simulate<Player, BasicPlayer>(10000);
    simulate<BasicPlayer, RandomPlayer>(10000);
    simulate<RandomPlayer, BasicPlayer>(10000);
    
    return 0;
}
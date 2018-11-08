
#include "game.hpp"
#include <iostream>
#include <random>

Game::Game() {
    this -> state = State();
}

int Game::play() {
    
    // setting up random stuff
    std::random_device rd;
    std::mt19937_64 mt(rd());
    std::uniform_int_distribution<int> zeroNineDist(0, 9);

    while (!(this -> state).gameOver()) { // while the game is not over
        if ((this -> state).whoseTurn() == 1) { // player 1's turn
            
            int r;
            do {
                r = zeroNineDist(mt);
            } while (!(this -> state).validMove((r % 3), (r / 3), 1));

            (this -> state).set((r % 3), (r / 3), 1);

        } else { // player -1's turn

            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    if ((this -> state).get(i, j) == 0) {
                        if ((this -> state).validMove(i, j, -1)) {
                            (this -> state).set(i, j, -1);
                            goto stop;
                        } else {
                            return 42; // YOU DUN FUCKED UP
                        }
                    }
                }
            }
            stop: ;

        }
        std::cout << (this -> state).string() << std::endl;
    }
    return (this -> state).winState();
}

std::string Game::string() const {
    return (this -> state).string();
}
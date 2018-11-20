
#ifndef GAME_HPP
#define GAME_HPP

#include "player.hpp"
#include "state.hpp"

#include <memory>

class Game {

private:
    State state;
    Player* p;
    Player* q;

public:
    Game(Player &p, Player &q) {
        this->p = &p;
        this->q = &q;
    };
    int play(); // actually play the game, return win state of board
    std::string string() const; // returns a string representation of the board
};

#endif
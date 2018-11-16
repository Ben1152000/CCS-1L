
#ifndef GAME_HPP
#define GAME_HPP

#include "player.hpp"
#include "state.hpp"

#include <memory>

class Game {

private:
    State state;
    std::unique_ptr<Player> p, q;

public:
    Game(std::unique_ptr<Player> p, std::unique_ptr<Player> q) :
        p(std::move(p)),
        q(std::move(q)) {}

    int play(); // actually play the game, return win state of board
    std::string string() const; // returns a string representation of the board
};

#endif
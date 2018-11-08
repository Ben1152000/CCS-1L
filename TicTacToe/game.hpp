
#ifndef GAME_HPP
#define GAME_HPP

#include "state.hpp"

class Game {

    private:
        State state;

    public:
        Game();                     // initializer
        int play();                 // actually play the game, return win state of board
        std::string string() const;                           // returns a string representation of the board

};

#endif
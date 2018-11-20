
#ifndef PLAYER_HPP
#define PLAYER_HPP

#include "state.hpp"
#include <string>

class Player {

    public:
        virtual void move(State, int, int&, int&, bool) {}
        virtual std::string type() {return "Player";}
    };

#endif
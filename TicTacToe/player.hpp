
#ifndef PLAYER_HPP
#define PLAYER_HPP

#include "state.hpp"

class Player {
public:
    virtual void move(State s, int value, int &i, int &j, bool invalid);
};

#endif
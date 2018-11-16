#ifndef RANDOM_PLAYER_HPP
#define RANDOM_PLAYER_HPP

#include "player.hpp"
#include "state.hpp"

#include <random>

class RandomPlayer : public Player {
private:
    std::mt19937_64 random;

public:
    RandomPlayer() : random(std::random_device{}()) {}
    virtual void move(
        State s, int value, int &i, int &j, bool invalid) override;
};

#endif
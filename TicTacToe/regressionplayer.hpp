
#ifndef REGRESSION_PLAYER_HPP
#define REGRESSION_PLAYER_HPP

#include "player.hpp"
#include "state.hpp"

#include <random>

class RegressionPlayer : public Player {

    private:
        std::mt19937_64 random;
        int weightings[3][3];

    public:
        RegressionPlayer() : random(std::random_device{}()) {}
        virtual void move(State s, int value, int &i, int &j, bool invalid) override;

};

#endif

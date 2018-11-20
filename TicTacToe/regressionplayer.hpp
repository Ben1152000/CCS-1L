
#ifndef REGRESSION_PLAYER_HPP
#define REGRESSION_PLAYER_HPP

#include "player.hpp"
#include "state.hpp"

#include <random>

class RegressionPlayer : public Player {

    private:
        std::mt19937_64 random;
        int weightings[9][27];

    public:
        RegressionPlayer();
        RegressionPlayer(const RegressionPlayer &source);
        virtual void move(State s, int value, int &i, int &j, bool invalid) override;
        virtual std::string type() override {return "RegressionPlayer";}
        std::string string();
        std::string name();

};

#endif


#ifndef BASIC_PLAYER_HPP
#define BASIC_PLAYER_HPP

#include "player.hpp"
#include "state.hpp"

#include <random>

class BasicPlayer : public Player {

    private:
        std::mt19937_64 random;

    public:
        BasicPlayer() : random(std::random_device{}()) {}
        virtual void move(State s, int value, int &i, int &j, bool invalid) override;
        virtual std::string type() override {return "BasicPlayer";}
};

#endif
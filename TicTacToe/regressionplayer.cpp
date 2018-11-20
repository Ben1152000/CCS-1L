
#include "regressionplayer.hpp"

#include <string>
#include <iostream>

RegressionPlayer::RegressionPlayer() : random(std::random_device{}()) {
    std::uniform_int_distribution<int> dist(-20, 20);
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 27; j++) {
            if (i * 3 == j || i * 3 + 2 == j) {
                this->weightings[i][j] = -1000; // discouraging bad behavior
            } else {
                this->weightings[i][j] = dist(random);
            }
        }
    }
    //std::cout << this->string(); // print the array
}

RegressionPlayer::RegressionPlayer(const RegressionPlayer &source) : random(std::random_device{}()) {
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 27; j++) {
            this->weightings[i][j] = source.weightings[i][j];
        }
    }
    int mutations = 10;
    for (int mutation = 0; mutation < mutations; mutation++) {
        std::uniform_int_distribution<int> dist(0, 9);
        std::uniform_int_distribution<int> dist2(0, 27);
        std::uniform_int_distribution<int> flip(0, 1);
        this->weightings[dist(random)][dist2(random)] += (flip(random) * 2) - 1;
    }
    //std::cout << this->string(); // print the array
}

void RegressionPlayer::move(State s, int /* value */, int &i, int &j, bool invalid) {
    if (invalid) { // if the last try was invalid, just pick one at random
        std::uniform_int_distribution<int> dist(0, 3);
        i = dist(random);
        j = dist(random);
        return;
    }
    int x[27] = {0}; // input vector
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            x[(3 * i + j) * 3 + s.get(i, j) + 1] = 1;
        }
    }
    int y[9] = {0}; // output vector
    for (int m = 0; m < 9; m++) {
        for (int n = 0; n < 27; n++) {
            y[m] += (this->weightings[m][n] * x[n]);
        }
    }
    int max = y[0];
    for (int m = 0; m < 9; m++) {
        if (y[m] > max) {
            max = y[m];
            i = m / 3;
            j = m % 3;
        }
    }
}

std::string RegressionPlayer::string() {
    std::string s = "";
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 27; j++) {
            s += std::to_string(this->weightings[i][j]) + " ";
        }
        s += "\n";
    }
    return s;
}

std::string RegressionPlayer::name() {
    std::string s = "";
    for (int i = 0; i < 9; i++) {
        int value = 26000;
        for (int j = 0; j < 27; j++) {
            value += this->weightings[i][j];
        }
        s += (char) ((value / 5) % 26 + 97);
    }
    return s;
}
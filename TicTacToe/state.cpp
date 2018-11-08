
#include "state.hpp"

State::State() {                                // constructor
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            this -> array[i][j] = 0;
        }
    }
}

int State::get(int i, int j) const {               // return state of indicated square
    return (this -> array)[i][j];
}

void State::set(int i, int j, int value) {
    (this -> array)[i][j] = value;
}

// State& State::operator=(const State& source){
//     for (int i = 0; i < 3; i++) {
//         for (int j = 0; j < 3; j++) {
//             this -> set(i, j, source.get(i, j));
//         }
//     }
//     return *this;
// }

std::string State::string() const {
    std::string s = "";
    for (int i = 0; i < 3; i++) {
        s += "[ ";
        for (int j = 0; j < 3; j++) {
            if (this -> get(i, j) == 1) s += "x";
            if (this -> get(i, j) == -1) s += "o";
            if (this -> get(i, j) == 0) s += "_";
            s += " ";
        }
        s += "]\n";
    }
    return s;
}

int State::whoseTurn() const {
    int sum = 0;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            sum += this -> get(i, j);
        }
    }
    return sum > 0 ? -1 : 1;
}

bool State::validMove(int i, int j, int value) const {
    return (value == this -> whoseTurn()) && (this -> get(i, j) == 0);
}

int State::winState() const {                         // returns the winning player or 0 if the game is tied
    if (get(0, 0) == get(0, 1) && get(0, 0) == get(0, 2)) return get(0, 0); // first row
    if (get(1, 0) == get(1, 1) && get(1, 0) == get(1, 2)) return get(1, 0); // second row
    if (get(2, 0) == get(2, 1) && get(2, 0) == get(2, 2)) return get(2, 0); // third row
    if (get(0, 0) == get(1, 0) && get(0, 0) == get(2, 0)) return get(0, 0); // first column
    if (get(0, 1) == get(1, 1) && get(0, 1) == get(2, 1)) return get(0, 1); // second column
    if (get(0, 2) == get(1, 2) && get(0, 2) == get(2, 2)) return get(0, 2); // third column
    if (get(0, 0) == get(1, 1) && get(0, 0) == get(2, 2)) return get(0, 0); // positive diagonal
    if (get(0, 2) == get(1, 1) && get(0, 2) == get(2, 0)) return get(0, 2); // negative diagonal
    return 0;
}

bool State::gameOver() const {
    if (this -> winState() != 0) return true;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (this -> get(i, j) == 0) return false;
        }
    }
    return true;
}


/*
bool Toe::makeMove(index x, int player) {   // makes a move if it is a valid move
    if (player == getPlayerTurn()) {
        if (getSquare(x.i, x.j) == 0) {
            setSquare(x.i, x.j, player);
            return true;
        }
    }
    return false;
}

int Toe::getPlayerTurn() {                       // returns the player whose turn it is, or 0 if the game is over
    int sum = 0;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            sum += getSquare(i, j);
        }
    }
    return sum > 0 ? -1 : 1;
}

*/
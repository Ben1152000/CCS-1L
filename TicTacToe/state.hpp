// state.h
// state class header

#ifndef STATE_HPP
#define STATE_HPP

#include <string>

class State {

private:
    int array[3][3]; // actual value of state

public:
    State();                           // constructor (initialize)
    int get(int i, int j) const;       // return state of indicated square
    void set(int i, int j, int value); // set state of square
    std::string string() const; // returns a string representation of the board
    int whoseTurn() const;      // player who goes next, or 0 if game over
    bool validMove(int i, int j, int value) const; // is move valid?
    int winState() const;  // winning player # or 0 if tie game
    bool gameOver() const; // returns 1 if the game is over, 0 if not
};

#endif
// state.h
// state class header

#ifndef STATE_HPP
#define STATE_HPP

#include <string>

class State {

    private:
        int array[3][3];                                // actual value of state

    public:
        State();                                        // constructor (initialize)
        int get(int i, int j) const;                          // return state of indicated square
        void set(int i, int j, int value);              // set state of square
        // State& operator=(const State& source);          //overloaded assignment operator
        std::string string() const;                           // returns a string representation of the board
        int whoseTurn() const;                                // returns the player whose turn it is, or 0 if the game is over
        bool validMove(int i, int j, int value) const;        // returns if a move is valid
        int winState() const;                                 // returns the winning player or 0 if the game is tied
        bool gameOver() const;                                // returns 1 if the game is over, 0 if not

};

#endif
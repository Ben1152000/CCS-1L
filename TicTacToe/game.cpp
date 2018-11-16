
#include "game.hpp"

#include "state.hpp"
#include "player.hpp"

#include <iostream>


int Game::play() {
    while (!(this->state).gameOver()) {       // while the game is not over
        if ((this->state).whoseTurn() == 1) { // player 1's turn

            int i, j = 0;
            bool valid = true;
            do { // loop until p spits out a valid move
                /* std::cout << "\nCurrent state:\n" << (this->state).string(); */
                /* std::cout << "Player 1 turn" << std::endl; */
                this->p->move(State(this->state), 1, i, j, !valid);
                /* std::cout << "Possible move: " << i << " " << j; */
                valid = (this->state).validMove(i, j, 1);
                /* std::cout << " valid=" << valid << std::endl; */
            } while (!valid);
            (this->state).set(i, j, 1); // actually make the move

        }
        else { // player -1's turn

            int i, j = 0;
            bool valid = true;
            do { // loop until p spits out a valid move
                /* std::cout << "\nCurrent state:\n" << (this->state).string(); */
                /* std::cout << "Player -1 turn" << std::endl; */
                this->q->move(State(this->state), -1, i, j, !valid);
                /* std::cout << "Possible move: " << i << " " << j; */
                valid = (this->state).validMove(i, j, -1);
                /* std::cout << " valid=" << valid << std::endl; */
            } while (!valid);
            (this->state).set(i, j, -1); // actually make the move

        }
        // Print out the current state of the board (for debugging)
        /* std::cout << (this->state).string() << std::endl; */
    }
    return (this->state).winState();
}

std::string Game::string() const { return (this->state).string(); }
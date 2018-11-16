
#include "basicplayer.hpp"

/* #include <iostream> */

void BasicPlayer::move(State s, int value, int &i, int &j, bool /* invalid */) {
    
    /* std::cout << s.string() << std::endl; */

    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            if (s.get(i, j) == 0) {
                s.set(i, j, value);
                if (s.gameOver() && s.winState() == value) {
                    /* std::cout << "Attack: " << i << " " << j << std::endl; */
                    return;
                }
                s.set(i, j, 0);
            }
        }
    }

    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            if (s.get(i, j) == 0) {
                
                s.set(i, j, -value);
                if (s.gameOver() && s.winState() == -value) {
                    /* std::cout << "Block: " << i << " " << j << std::endl; */
                    return;
                }
                s.set(i, j, 0);
            }
        }
    }

    std::uniform_int_distribution<int> dist(0, 3);
    i = dist(random);
    j = dist(random);

    /* std::cout << "Random: " << i << " " << j << std::endl; */
    return;
}
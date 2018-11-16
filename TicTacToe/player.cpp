
#include "player.hpp"

// This is a sample ai function
void Player::move(
    State s, int /* value */, int &i, int &j, bool /* invalid */) {
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            if (s.get(i, j) == 0) { return; }
        }
    }
}

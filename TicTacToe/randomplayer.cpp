
#include "randomplayer.hpp"

void RandomPlayer::move( State /* s */, int /* value */, int &i, int &j, bool /* invalid */) {
    std::uniform_int_distribution<int> dist(0, 3);
    i = dist(random);
    j = dist(random);
    return;
}
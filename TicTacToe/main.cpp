
#include "state.hpp"
#include "game.hpp"
#include <iostream>

using namespace std;

int main() {
    Game game;
    int sum = 0;
    for (int i = 0; i < 1000; i++) {
        game = Game();
        sum += game.play();
    }
    cout << sum << endl;

    return 0;
}
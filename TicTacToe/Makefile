# Makefile

COMPILER = g++
CXX_FLAG = --std=c++11 -g

all: main

main: main.o state.o player.o game.o
	$(COMPILER) $(CXX_FLAG) -o main main.o state.o player.o game.o

main.o: main.cpp
	$(COMPILER) -c $(CXX_FLAG) main.cpp

state.o: state.cpp
	$(COMPILER) -c $(CXX_FLAG) state.cpp

player.o: player.cpp
	$(COMPILER) -c $(CXX_FLAG) player.cpp

game.o: game.cpp
	$(COMPILER) -c $(CXX_FLAG) game.cpp

clean:
	rm -f *.o
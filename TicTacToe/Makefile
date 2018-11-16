# Makefile

CXX_WARNINGS = -Wall -Wconditional-uninitialized -Wconversion -Wcovered-switch-default -Wdeprecated -Wextra -Wimplicit -Winvalid-noreturn -Wmissing-noreturn -Wmissing-prototypes -Wmissing-variable-declarations -Wnewline-eof -Wshadow-all -Wno-logical-op-parentheses -Wno-shorten-64-to-32 -Wno-sign-compare -Wno-sign-conversion -Wnon-virtual-dtor -Wtautological-compare -Wthread-safety -Wunreachable-code-aggressive -Wuninitialized -Wunused -Werror=implicit-fallthrough -Werror=old-style-cast -Werror=return-type -Werror=switch -Werror=unused-result -Werror=zero-as-null-pointer-constant

CXX = clang++
CXXFLAGS = -std=c++17 -Og -g3 -Wall -Wextra
LD = $(CXX)
LDFLAGS =

OBJS = game.o main.o state.o player.o randomplayer.o basicplayer.o

all: main

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c -o $@ $^

main: $(OBJS)
	$(LD) $(LDFLAGS) -o $@ $^

clean:
	rm -f main $(OBJS)
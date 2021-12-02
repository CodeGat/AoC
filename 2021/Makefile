all: $(patsubst %.cpp, %.o, $(wildcard *.cpp))

%.o: %.cpp Makefile
	g++ $< -g -o ./build/$@

clean:
	rm -r ./build/
	mkdir build

d2p1:
	@/usr/bin/time -f "Program executed: took %es" ./build/$@.o "input/$@.txt" 

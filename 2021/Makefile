all: $(patsubst %.cpp, %.o, $(wildcard *.cpp))

%.o: %.cpp
	g++ $^ -g -o ./build/$@

clean:
	rm -r ./build/
	mkdir build

%: %.o
	@/usr/bin/time -f "Program executed: took %es" ./build/$^ "input/$@.txt" 

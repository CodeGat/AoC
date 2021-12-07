all: $(patsubst %.cpp, %.o, $(wildcard *.cpp))

%.o: %.cpp
	g++ $^ -g -I /mnt/c/Users/Tommi/Installations/boost_1_77_0 -o ./build/$@

clean:
	rm -r ./build/
	mkdir build

%: %.o
	@/usr/bin/time -f "Program executed: took %es" ./build/$^ "input/$@.txt" 

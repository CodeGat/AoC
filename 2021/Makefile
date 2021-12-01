run:
	g++ $(FILE).cpp -g -o ./build/$(FILE).o
	@/usr/bin/time -f "Program executed: took %es" ./build/$(FILE).o "input/$(FILE).txt"
cleanall:
	rm ./build/*.o

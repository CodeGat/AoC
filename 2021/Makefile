run:
	gcc $(FILE).c -g -o ./build/$(FILE).o
	@/usr/bin/time -f "Program executed: took %es" ./build/$(FILE).o
cleanall:
	rm ./build/*.o

#include <iostream>
#include <fstream>
#include <limits>
using namespace std;

int main(int argc, char **argv){
	ifstream in (argv[1]); // input file
	int lastNumber = numeric_limits<int>::max();
	int amountOfIncreasingNumbers = 0;
	int number;

	while (in >> number)  {
		if (number > lastNumber) {
			amountOfIncreasingNumbers = amountOfIncreasingNumbers + 1;
		}
		lastNumber = number;
	}

	printf("%d", amountOfIncreasingNumbers);
	return 0;
}



#include <iostream>
#include <fstream>
#include <limits>
using namespace std;

int main(int argc, char **argv)
{
	ifstream in (argv[1]);
	int last_number = numeric_limits<int>::max();
	int number_of_increasing_numbers = 0;
	int number;

	while (in >> number)  {
		if (number > last_number) {
			number_of_increasing_numbers = number_of_increasing_numbers + 1;
		}
		last_number = number;
	}

	printf("%d", number_of_increasing_numbers);
	return 0;
}



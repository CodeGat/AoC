#include <iostream>
#include <fstream>
#include <limits>
using namespace std;

// Imitates the 'sliding window' - shuffles all the elements of the array down one, dropping off the last element and adding the new number to the front of the array
void slideWindowUsing(int (&array)[3], int numberToAdd){
	array[2] = array[1];
	array[1] = array[0];
	array[0] = numberToAdd;

}

int main(int argc, char **argv){
	ifstream in (argv[1]); // the input file
	int slidingWindow[3];
	int initSlidingWindowIx = 2; //used to initialize the first three numbers in the array
	int oldSum = numeric_limits<int>::max();
	int currentSum = numeric_limits<int>::max();
	int number;
	int amountOfIncreasingSums = 0; //  the result we need

	while (in >> number){ // while we still have numbers in the input file, assign 'number' the current number we are up to
		if (initSlidingWindowIx > -1){ //if we still have to add numbers to the array initially
			slidingWindow[initSlidingWindowIx] = number;
			initSlidingWindowIx = initSlidingWindowIx - 1; // add it from the back of the array
		} else {
			oldSum =  currentSum;
			slideWindowUsing(slidingWindow, number); //slide the 'window' down the array, adding the current number and dropping off the oldest
			currentSum = slidingWindow[0] + slidingWindow[1] + slidingWindow[2];

			if (currentSum > oldSum){
				amountOfIncreasingSums++;
			}
		}
	}

	printf("%d\n", amountOfIncreasingSums);

	return 0;
}



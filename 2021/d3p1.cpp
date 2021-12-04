#include <fstream>
#include <iostream>
#include <bitset>
using namespace std;

#define HORIZ_BIT_SIZE 12
#define VERT_BIT_SIZE 1000

int main(int argc, char **argv){
    ifstream in (argv[1]);
    bitset<VERT_BIT_SIZE> bits[HORIZ_BIT_SIZE]; //hardcoded, bad! >:( But dont wanna import boost/dynamic_bitset.hpp

    for (int col = 0; col < HORIZ_BIT_SIZE; col++) {
        char verticalBits[VERT_BIT_SIZE];
        for (int row = 0; row < VERT_BIT_SIZE; row++) {
            in.seekg(row * HORIZ_BIT_SIZE + col + row, ios::beg); //read from top-bottom, then left-right!
            char bit[1];
            in.read(bit, 1); //read a single 'bit'
            verticalBits[row] = bit[0];
        }

        bits[col] = bitset<VERT_BIT_SIZE>(verticalBits); //convert the top-to-bottom 'bits' to a bitset and add to array 
    }

    char gammaString[HORIZ_BIT_SIZE];
    for (auto i = 0; i < HORIZ_BIT_SIZE; i++){ //for each chunk of vertical bits we'd just made...
        if (bits[i].count() > VERT_BIT_SIZE / 2){ // if theres more 1s than 0s...
            gammaString[i] = '1'; //add one to that position in the gammaString
        } else {
            gammaString[i] = '0'; //or zero if not
        }
    }

    bitset<HORIZ_BIT_SIZE> gammaBits (gammaString);
    bitset<HORIZ_BIT_SIZE> epsilonBits = ~gammaBits; // epsilon is just the opposite bits to gamma!

    // could also do transpose char** then forall bitset<size> (allbits[i]).count > size ? gamma += 1 : gamma += 0
    // O(n^2) complexity for transpose ^

    printf("%lu\n", gammaBits.to_ulong() * epsilonBits.to_ulong());

    return 0;
}
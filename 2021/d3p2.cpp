#include <fstream>
#include <iostream>
#include <bitset>
#include <vector>
using namespace std;

#define HORIZ_BIT_SIZE 12 //hardcode bad

bitset<HORIZ_BIT_SIZE> findBitCriteriaUsing(vector<bitset<HORIZ_BIT_SIZE>> bits, int bitToCheck){

    for (auto horizBit = HORIZ_BIT_SIZE - 1; horizBit >= 0; horizBit--){
        vector<bitset<HORIZ_BIT_SIZE>> onesAtBitNo;
        vector<bitset<HORIZ_BIT_SIZE>> zerosAtBitNo;

        if (bits.size() == 1) {
            cout << "only one to go! = " << bits[0] << endl;
            break;
        }

        for (size_t vertBit = 0; vertBit < bits.size(); vertBit++){
            if (bits[vertBit].test(horizBit)) {
                onesAtBitNo.push_back(bits[vertBit]);
            } else {
                zerosAtBitNo.push_back(bits[vertBit]);
            }
        }

        if (bitToCheck == 1){
            if (onesAtBitNo.size() >= zerosAtBitNo.size()){
                bits = onesAtBitNo;
            } else {
                bits = zerosAtBitNo;
            }
        } else {
            if (onesAtBitNo.size() < zerosAtBitNo.size()){
                bits = onesAtBitNo;
            } else {
                bits = zerosAtBitNo;
            }
        }

    }

    for (int i = 0; i < bits.size(); i++){
        cout << bits[i] << endl;
    }
    cout << "~~~~~~~" << endl;

    return bits[0];
}

int main(int argc, char **argv){
    ifstream in (argv[1]);

    vector<bitset<HORIZ_BIT_SIZE>> bits;
    string line;
    while (in >> line){ //O(n)
        bits.push_back(bitset<HORIZ_BIT_SIZE>(line));
    }

    bitset<HORIZ_BIT_SIZE> oxygenGeneratorRatingBits (findBitCriteriaUsing(bits, 1));
    bitset<HORIZ_BIT_SIZE> co2ScrubberRatingBits (findBitCriteriaUsing(bits, 0));

    std::printf("oxy: %lu, co2: %lu\n", oxygenGeneratorRatingBits.to_ulong(), co2ScrubberRatingBits.to_ulong());
    std::printf("%lu\n", oxygenGeneratorRatingBits.to_ulong() * co2ScrubberRatingBits.to_ulong()); //old: 484706

    return 0;
}
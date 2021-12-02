#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(int argc, char **argv){
    ifstream in (argv[1]);
    string direction;
    string amount;
    int horizontal = 0;
    int vertical = 0;
    int aim = 0;

    while (in >> direction >> amount){
        if (direction == "forward"){
            horizontal += stoi(amount);
            vertical += aim * stoi(amount);
        } else if (direction == "up"){
            aim -= stoi(amount);
        } else if (direction == "down"){
            aim += stoi(amount);
        }
    }

    printf("Result: %d\n", horizontal * vertical);
    return 0;
}
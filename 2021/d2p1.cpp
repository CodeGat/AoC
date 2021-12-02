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

    while (in >> direction >> amount){
        if (direction == "forward"){
            horizontal += stoi(amount);
        } else if (direction == "up"){
            vertical -= stoi(amount);
        } else if (direction == "down"){
            vertical += stoi(amount);
        } else {
            cout << "Something happened" << endl;
        }
    }

    printf("Result: %d\n", horizontal * vertical);
    return 0;
}
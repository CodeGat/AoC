#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
#define BOARD_DIM 5

typedef struct {
    int value;
    bool ticked = 0;
} cell;

vector<int> createNumbers(string line);
void checkSolution(vector<vector<cell>> boards, int boardNo, int number, bool &winner);
void tickNumber(vector<vector<cell>> &boards, int boardNo, int number);

int main(int argc, char **argv){
    ifstream in (argv[1]);

    vector<int> numbers;
    vector<vector<cell>> boards;

    string line;
    bool firstLine = true;
    int cellCount = 0;
    vector<cell> potentialBoard;

    // getting input
    while (in >> line) {
        if (firstLine) {
            numbers = createNumbers(line);
            firstLine = false;
        } else {
            cell boardCell = { stoi(line) };
            potentialBoard.push_back(boardCell);
            cellCount++;

            if (cellCount == BOARD_DIM * BOARD_DIM) {
                cellCount = 0;
                boards.push_back(potentialBoard);
                potentialBoard.clear();
            }
        }
    }
    in.close();

    //playing the actual game
    bool winner = false;
    vector<cell> winningBoard;
    int winningNumber;
    for (int number: numbers) {
        for (int boardNo = 0; boardNo < boards.size(); boardNo++) {    
            tickNumber(boards, boardNo, number);
            checkSolution(boards, boardNo, number, winner);

            if (winner) {
                winningBoard = boards[boardNo];
                winningNumber = number;
                break;
            }
        }
        if (winner) {
            break;
        }
    }

    //calculating result
    int result = 0;
    for (cell c: winningBoard) {
        if (!c.ticked) {
            result += c.value;
        }
    }
    result *= winningNumber;

    printf("Score: %d\n", result);

    return 0;
}

vector<int> createNumbers(string line){
    vector<int> numbers;
    size_t pos = 0;
    while ((pos = line.find(',')) != string::npos){
        string number = line.substr(0, pos);
        
        numbers.push_back(stoi(number));
        line.erase(0, pos + 1);
    }
    numbers.push_back(stoi(line));

    return numbers;
}

void checkSolution(vector<vector<cell>> boards, int boardNo, int number, bool &winner) {

    // future improvement? check board[X, Y] AND board[Y, X] at same time? Wouldn't allow breaking. Could be less complex.
    //check rows 
    for (int row = 0; row < BOARD_DIM; row++) {
        for (int col = 0; col < BOARD_DIM; col++) {
            if (!(boards[boardNo][row * BOARD_DIM + col].ticked)) {
                break;
            } else if (col == BOARD_DIM - 1 && boards[boardNo][row * BOARD_DIM + col].ticked) {
                winner = true;
                return;
            } else {
                continue;
            }
        }
    }

    //check columns
    for (int col = 0; col < BOARD_DIM; col++) {
        for (int row = 0; row < BOARD_DIM; row++) {
            if (!(boards[boardNo][row * BOARD_DIM + col].ticked)) {
                break;
            } else if (row == BOARD_DIM - 1 && boards[boardNo][row * BOARD_DIM + col].ticked) {
                winner = true;
                return;
            } else {
                continue;
            }
        }
    }
}

void tickNumber(vector<vector<cell>> &boards, int boardNo, int number) {
    for (auto &c: boards[boardNo]) {
        if (c.value == number) {
            c.ticked = true;
        }
    }
}

#include <fstream>
#include <iostream>
#include <vector>
#include <string>
using std::ifstream;
using std::string;
using std::vector;
using std::fill;
#define FLOOR_DIM 100000

//could do chunks of arrays?
//could check foreach point in each line?

typedef struct {
    unsigned int x;
    unsigned int y;
} point;
typedef struct {
    point p1;
    point p2;
} line;

point getCoord(string coordString);
void writeCheckVerticalLine(line line, unsigned &dangerousPoints, unsigned (&floor)[FLOOR_DIM][FLOOR_DIM]);
void writeCheckHorizontalLine(line line, unsigned &dangerousPoints, unsigned (&floor)[FLOOR_DIM][FLOOR_DIM]);

int main(int argc, char **argv) {
    ifstream  in (argv[1]);

    static unsigned floor[FLOOR_DIM][FLOOR_DIM] = {{0}};
    vector<line> lines;
    unsigned dangerousPoints = 0;

    // format input
    string xy1, sep, xy2;
    while (in >> xy1 >> sep >> xy2) {
        point from = getCoord(xy1);
        point to = getCoord(xy2);

        if (from.x == to.x || from.y == to.y) {
            lines.push_back(line { from, to });
        }
    }
    in.close();

    // write lines to floor
    for (line line: lines) {
        if (line.p1.x == line.p2.x) { // it must be a horizontal line 
            writeCheckHorizontalLine(line, dangerousPoints, floor);
        } else if (line.p1.y == line.p2.y) { // it must be a vertical line
            writeCheckVerticalLine(line, dangerousPoints, floor);
        }
    }

    // get result
    printf("The number of dangerous points is: %d\n", dangerousPoints);

    return 0;
}

point getCoord(string coordString) {
    int pos = coordString.find(',');
    string x = coordString.substr(0, pos);
    string y = coordString.substr(pos + 1, coordString.size());

    return point { (unsigned)stoi(x), (unsigned)stoi(y) };
}

void writeCheckVerticalLine(line line, unsigned &dangerousPoints, unsigned (&floor)[FLOOR_DIM][FLOOR_DIM]) {
    if (line.p1.x < line.p2.x) { // p1 is the beginning of the vertical line
        for (unsigned segment = line.p1.x; segment <= line.p2.x; segment++){
            floor[line.p1.y][segment] += 1;
            if (floor[line.p1.y][segment] > 1) {
                dangerousPoints++;
            }
        }
    } else { // p2 is the beginning of the line
        for (unsigned segment = line.p2.x; segment <= line.p1.x; segment++){
            floor[line.p1.y][segment] += 1;
            if (floor[line.p1.y][segment] > 1) {
                dangerousPoints++;
            }
        }
    }
}

void writeCheckHorizontalLine(line line, unsigned &dangerousPoints, unsigned (&floor)[FLOOR_DIM][FLOOR_DIM]){
    if (line.p1.y < line.p2.y) { // p1 is the beginning of the vertical line
        for (unsigned segment = line.p1.y; segment <= line.p2.y; segment++){
            floor[segment][line.p1.x] += 1;
            if (floor[segment][line.p1.x] > 1) {
                dangerousPoints++;
            }
        }
    } else { // p2 is the beginning of the line
        for (unsigned segment = line.p2.y; segment <= line.p1.y; segment++){
            floor[segment][line.p1.x] += 1;
            if (floor[segment][line.p1.x] > 1) {
                dangerousPoints++;
            }
        }
    }
}
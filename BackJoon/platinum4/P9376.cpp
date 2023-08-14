#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

template <typename T>
void print_map(T** map, int row, int col) {
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			cout << map[i][j];
		}
		cout << "\n";
	}
}

struct point {
	int _row, _col;

	point(int _row, int _col) :_row(_row), _col(_col) {};
};


int solution(char** map, int row, int col) {

	vector<point> start;
	start.push_back(point(0, 0));

	int** detect_map = new int* [row];

	for (int i = 0; i < row; i++) {
		detect_map[i] = new int[col];
		for (int j = 0; j < col; j++) {
			detect_map[i][j] = 0;
			if (map[i][j] == '$') {
				start.push_back(point(i, j));
			}
		}
	}

	// down, up, left, right
	point move[4] = { point(1, 0), point(-1, 0), point(0, 1), point(0, -1) };

	for (vector<point>::iterator itr = start.begin(); itr != start.end(); ++itr) {
		point _start = *itr;

		int** door_map = new int * [row];
		for (int i = 0; i < row; i++) {
			door_map[i] = new int[col];
			for (int j = 0; j < col; j++) {
				door_map[i][j] = -1;
			}
		}

		queue<point> q;
		q.push(_start);
		door_map[_start._row][_start._col] = 0;

		while (!q.empty()) {
			point cur = q.front();
			q.pop();

			for (int m = 0; m < 4; m++) {
				int m_row = cur._row + move[m]._row;
				int m_col = cur._col + move[m]._col;

				if (0 <= m_row && m_row < row && 0 <= m_col && m_col < col) {
					if (map[m_row][m_col] != '*' && door_map[m_row][m_col] == -1) {
						q.push(point(m_row, m_col));

						if (map[m_row][m_col] == '#') {
							door_map[m_row][m_col] = door_map[cur._row][cur._col] + 1;
						}
						else {
							door_map[m_row][m_col] = door_map[cur._row][cur._col];
						}
					}
				}
			}
		}

		//print_map(door_map, row, col);

		for (int i = 0; i < row; i++) {
			for (int j = 0; j < col; j++) {
				if (map[i][j] != '*') {
					detect_map[i][j] += door_map[i][j];
				}
			}
		}
	}

	//print_map(detect_map, row, col);

	int min_value = INT32_MAX;
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			if (map[i][j] != '*') {
				if (map[i][j] == '#' && min_value > detect_map[i][j] - 2) {
					min_value = detect_map[i][j] - 2;
				}
				else if(map[i][j] == '.' && min_value > detect_map[i][j]) {
					min_value = detect_map[i][j];
				}
			}
		}
	}

	return min_value;
}


int main() {
	cin.tie(NULL)->sync_with_stdio(false);

	int task_n;

	cin >> task_n;

	for (int i = 0; i < task_n; i++) {
		int row, col;
		cin >> row >> col;

		char** map = new char* [row + 2];
		for (int i = 0; i < row + 2; i++) {
			map[i] = new char[col + 2];
			for (int j = 0; j < col + 2; j++) {
				map[i][j] = '.';
			}
		}

		for (int i = 1; i < row + 1; i++) {
			string line;
			cin >> line;
			for (int j = 1; j < col + 1; j++) {
				map[i][j] = line[j - 1];
			}
		}

		//print_map(map, row + 2, col + 2);

		cout << solution(map, row + 2, col + 2) << "\n";
	}

	return 0;
}
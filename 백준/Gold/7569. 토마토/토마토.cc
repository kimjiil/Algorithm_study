#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int col, row, h;

// 1: 익은 토마토, 0 : 익지 않은 토마토, -1: 토마토가 들어있지 않는 칸

void print_map(int*** map) {

	for (int k = 0; k < h; k++) {
		for (int i = 0; i < row; i++) {
			for (int j = 0; j < col; j++) {
				if (map[k][i][j] == -1) {
					cout << map[k][i][j] << " ";
				}
				else {
					cout << " " << map[k][i][j] << " ";
				}
			}
			cout << "\n";
		}
		cout << "=============================\n";
	}

}

class point {
public:
	int h, row, col;
	int day;

	point(int h, int row, int col, int day) :h(h), row(row), col(col), day(day) {}

	point operator+(const point& other) {
		return point(h + other.h, row + other.row, col + other.col, day + other.day + 1);
	}
};

int main() {
	cin.tie(NULL)->sync_with_stdio(false);

	cin >> col >> row >> h;

	int*** map = new int** [h];
	int day=0;

	queue<point> ripe_tomato;
	for (int k = 0; k < h; k++) {
		map[k] = new int* [row];
		for (int i = 0; i < row; i++) {
			map[k][i] = new int[col];

			for (int j = 0; j < col; j++) {
				cin >> map[k][i][j];

				if (map[k][i][j] == 1) {
					ripe_tomato.push(point(k, i, j, 0));
				}

			}
		}
	}

	//up_h, donw_h , down, right, up, left,
	point move_point[6] = {point(1,0,0, 0),point(-1,0,0, 0), point(0, 1, 0, 0), 
		point(0, 0, 1, 0), point(0, -1, 0, 0), point(0, 0 ,-1, 0) };

	while (!ripe_tomato.empty()) {
		point cur = ripe_tomato.front();
		ripe_tomato.pop();

		for (int i = 0; i < 6; i++) {
			point mov_p = cur + move_point[i];
			if (0 <= mov_p.col && mov_p.col < col && 0 <= mov_p.row && mov_p.row < row && 0 <= mov_p.h && mov_p.h < h) {
				if (map[mov_p.h][mov_p.row][mov_p.col] == 0) {
					map[mov_p.h][mov_p.row][mov_p.col] = 1;
					ripe_tomato.push(mov_p);
					day = mov_p.day;
					//cout << day << "\n";
				}
			}
		}
		//print_map(map);
	}

	bool is_all_ripe = true;
	for (int k = 0; k < h; k++) {
		for (int i = 0; i < row; i++) {
			for (int j = 0; j < col; j++) {
				if (map[k][i][j] == 0) {
					is_all_ripe = false;
					break;
				}
			}
		}
	}

	//print_map(map);
	if (is_all_ripe) {
		cout << day;
	}
	else {
		cout << -1;
	}

	return 0;
}
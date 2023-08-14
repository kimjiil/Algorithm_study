#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

int ROW, COL;

struct point {
	int row, col;
	int direction;

	point(int row, int col) : row(row), col(col) {
		direction = -1;
	}

	point(const point& p, int direction) : row(p.row), col(p.col), direction(direction) {}

	point(int row, int col, int direction) : row(row), col(col), direction(direction) {}
};

template <typename T>
void print_map(T** map, int direction = 0) {
	cout << "-----------------------------------\n";
	for (int i = 0; i < ROW; i++) {
		for (int j = 0; j < COL; j++) {
			string tmp = to_string(map[i][j][direction]);
			if (tmp.length() == 3) {
				cout << tmp;
			}
			else if (tmp.length() == 2) {
				cout << " " << tmp;
			}
			else if (tmp.length() == 1) {
				cout << "  " << tmp;
			}
			else {
				cout << "  X";
			}
		}
		cout << "\n";
	}
}

int solution(char** map, vector<point> ps) {

	// down, right, up, left
	point move[4] = { point(1, 0), point(0, 1),point(-1, 0), point(0, -1) };

	int*** mirror_map = new int** [ROW];
	for (int i = 0; i < ROW; i++) {
		mirror_map[i] = new int*[COL];
		for (int j = 0; j < COL; j++) {
			mirror_map[i][j] = new int[4];
			for (int k = 0; k < 4; k++) {
				mirror_map[i][j][k] = INT32_MAX;
			}
		}
	}

	queue<point> bfs_q;
	//for (int i = 0; i < 4; i++) {
	//	bfs_q.push(point(ps[0], i));
	//	mirror_map[ps[0].row][ps[0].col][i] = 0;
	//}
	bfs_q.push(point(ps[0]));
	for (int i = 0; i < 4; i++) {
		mirror_map[ps[0].row][ps[0].col][i] = 0;
	}
	while (!bfs_q.empty()) {
		point cur = bfs_q.front();
		bfs_q.pop();

		for (int i = 0; i < 4; i++) {
			int mov_r = cur.row + move[i].row;
			int mov_c = cur.col + move[i].col;

			if (0 <= mov_r && mov_r < ROW && 0 <= mov_c && mov_c < COL) {
				if (map[mov_r][mov_c] != '*') {
					//bfs_q.push(point(mov_r, mov_c, i));

					if (cur.direction == -1) { //시작 지점
						bfs_q.push(point(mov_r, mov_c, i));
						mirror_map[mov_r][mov_c][i] = mirror_map[cur.row][cur.col][0];
					}
					else if (cur.direction % 2 != i % 2) { //직각 방향으로 움직일경우
						if (mirror_map[mov_r][mov_c][i] > mirror_map[cur.row][cur.col][cur.direction] + 1) {
							bfs_q.push(point(mov_r, mov_c, i));
							mirror_map[mov_r][mov_c][i] = mirror_map[cur.row][cur.col][cur.direction] + 1;
						}
					}
					else { // 평행 방향으로 움직일 경우
						if (mirror_map[mov_r][mov_c][i] > mirror_map[cur.row][cur.col][cur.direction]) {
							bfs_q.push(point(mov_r, mov_c, i));
							mirror_map[mov_r][mov_c][i] = mirror_map[cur.row][cur.col][cur.direction];
						}
					}
				}
			}
		}
	}

	int min_v = INT32_MAX;
	for (int i = 0; i < 4; i++) {
		//cout << mirror_map[ps[1].row][ps[1].col][i] << " ";
		if (mirror_map[ps[1].row][ps[1].col][i] != -1) {
			min_v = min(min_v, mirror_map[ps[1].row][ps[1].col][i]);
		}
	}
	//cout << "\n";

	/*for (int i = 0; i < 4; i++) {
		print_map(mirror_map, i);
	}*/

	return min_v;
}

int main() {
	cin.tie(NULL)->sync_with_stdio(false);

	cin >> COL >> ROW;

	char** map = new char*[ROW];

	vector<point> c_points;

	for (int i = 0; i < ROW; i++) {
		map[i] = new char[COL];
		string tmp;
		cin >> tmp;
		for (int j = 0; j < COL; j++) {
			map[i][j] = tmp[j];
			if (map[i][j] == 'C') {
				c_points.push_back(point(i, j));
			}
		}
	}

	cout << solution(map, c_points) << "\n";

	return 0;
}
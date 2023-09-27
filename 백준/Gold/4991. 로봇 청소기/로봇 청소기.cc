#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <math.h>

using namespace std;

int col, row;

int bit_check = 0b1111111111;
class point {
public:
	int row, col;
	int move;
	point() {
		row = 0;
		col = 0;
		move = 0;
	}
	point(int row, int col) : row(row), col(col) {
		move = 0;
	}
	point(int row, int col, int move) : row(row), col(col), move(move) {}

	point operator+(const point& other) {
		return point(row + other.row, col + other.col, move + 1);
	}

	bool operator==(const point& other) {
		if (row == other.row && col == other.col) {
			return true;
		}
		return false;
	}
};

void refresh(int** visited, point cur) {
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			visited[i][j] = 0;
		}
	}
	visited[cur.row][cur.col] = 1;
}

template <typename T>
void print_map(T** map, int row, int col) {
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			string tmp = to_string(map[i][j]);
			for (int l = 0; l < 3 - tmp.length(); l++) {
				cout << " ";
			}
			cout << map[i][j] << " ";
		}
		cout << "\n";
	}
	cout << "=================================\n";
}

class route {
public:
	//vector<int> route_list;
	int route_list;
	int cost;
	int cur;
	string tmp;
	route(int start, int len) {
		route_list = 0;
		cost = 0;
		cur = start;
		route_list = route_list | (1 << start);
		//tmp = to_string(start);
	}

	route(const route& r, int cost, int idx) {
		route_list = r.route_list;
		this->cost = r.cost + cost;
		cur = idx;
		route_list = route_list | (1 << idx);
		//tmp = r.tmp + to_string(cur);
	}
	bool is_visited(int idx) {
		return route_list & (1 << idx);
	}

	int current() {
		return cur;
	}
};

int solution() {

	point m_p[4] = { point(1, 0), point(0, 1), point(-1, 0), point(0, -1) };

	int start;
	vector<point> p_list;

	char** map = new char* [row];
	int** visited = new int* [row];
	for (int i = 0; i < row; i++) {
		map[i] = new char[col];
		visited[i] = new int[col];
		for (int j = 0; j < col; j++) {
			cin >> map[i][j];
			if (map[i][j] == 'o' || map[i][j] == '*') {
				p_list.push_back(point(i, j));
				if (map[i][j] == 'o') {
					start = p_list.size() - 1;
				}
			}
			visited[i][j] = 0;
		}
	}

	int** dist_map = new int* [p_list.size()];
	for (int i = 0; i < p_list.size(); i++) {
		dist_map[i] = new int[p_list.size()];
		for (int j = 0; j < p_list.size(); j++) {
			dist_map[i][j] = 999;
		}
	}

	for (int idx = 0; idx < p_list.size(); idx++) {
		queue<point> dfs_q;
		dfs_q.push(p_list[idx]);
		//visited[p_list[idx].row][p_list[idx].col] = 1;
		refresh(visited, p_list[idx]);

		while (!dfs_q.empty()) {
			point cur = dfs_q.front();
			dfs_q.pop();

			for (int i = 0; i < 4; i++) {
				point m = cur + m_p[i];
				if (0 <= m.col && m.col < col && 0 <= m.row && m.row < row) {
					if (visited[m.row][m.col] == 0 && map[m.row][m.col] != 'x') {
						dfs_q.push(m);
						visited[m.row][m.col] = 1;
						if (map[m.row][m.col] == '*' || map[m.row][m.col] == 'o') {
							for (int j = idx + 1; j < p_list.size(); j++) {
								if (m == p_list[j]) {
									dist_map[idx][j] = m.move;
									dist_map[j][idx] = m.move;
								}
							}
						}
					}
				}
			}
		}
		//print_map(dist_map, p_list.size(), p_list.size());
		//cout << "==============================\n";
	}
	queue<route> r_v;
	vector<route> end;
	r_v.push(route(start, p_list.size()));

	int route_dist_min = 2147483647;
	int bit_chech = pow(2, p_list.size()) - 1;
	while (!r_v.empty()) {
		// 시작점
		route tmp = r_v.front();
		r_v.pop();

		if (tmp.route_list == bit_chech) {
			if (route_dist_min > tmp.cost) {
				route_dist_min = tmp.cost;
			}
		}
		else {

			for (int i = 0; i < p_list.size(); i++) {
				if (!tmp.is_visited(i) && dist_map[tmp.current()][i] != 999) {
					r_v.push(route(tmp, dist_map[tmp.current()][i], i));
				}
			}
		}
	}


	if (route_dist_min == 2147483647) {
		return -1;
	}
	return route_dist_min;
}

int main() {
	cin.tie(NULL)->sync_with_stdio(false);

	while (true) {
		cin >> col >> row;

		if (col == 0 || row == 0) {
			break;
		}

		cout << solution() << "\n";
	}

	return 0;
}
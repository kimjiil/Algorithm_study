#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

int n, m;


void print_map(int** map) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cout << map[i][j] << " ";
		}
		cout << "\n";
	}
}

int main() {

	cin.tie(NULL)->sync_with_stdio(false);
	
	cin >> n >> m;

	int** map = new int* [n];
	for (int i = 0; i < n; i++) {
		string tmp_str;

		cin >> tmp_str;
		map[i] = new int[m];
		for (int j = 0; j < m; j++) {
			map[i][j] = tmp_str[j] - '0' - 1;
		}
	}

	int m_x[4] = { 1, -1, 0 , 0 };
	int m_y[4] = { 0 , 0 , 1 , -1 };
	
	queue<pair<int, int>> bfs_q; // (x, y)

	bfs_q.push(make_pair(0, 0));
	map[0][0] = 1;

	while (!bfs_q.empty()) {
		pair<int, int> cur = bfs_q.front();
		bfs_q.pop();

		for (int dir = 0; dir < 4; dir++) {
			int _x = cur.first + m_x[dir];
			int _y = cur.second + m_y[dir];

			if (0 <= _x && _x < m && 0 <= _y && _y < n) {
				if (map[_y][_x] == 0) {
					map[_y][_x] = map[cur.second][cur.first] + 1;
					bfs_q.push(make_pair(_x, _y));
				}
			}
		}
	}

	//print_map(map);

	cout << map[n - 1][m - 1];
	return 0;
}
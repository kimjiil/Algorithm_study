#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

int m, n, k;

void print_map(int** maps) {

	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			if (maps[i][j] == -1) {
				cout << maps[i][j] << " ";
			}
			else {
				cout << " " << maps[i][j] << " ";
			}
		}
		cout << "\n";
	}
}


struct point {
	int x, y;

	point(int x, int y) : x(x), y(y) {}

	point operator+(const point& other) {
		return point(x + other.x, y + other.y);
	}
};

int dfs(int** maps, int x, int y) {

	// right, up, left, down
	point move[4] = { point(1, 0), point(0 , 1), point(-1, 0), point(0 , -1) };
	
	queue<point> dfs_q;

	dfs_q.push(point(x, y));
	maps[y][x] = 1;
	
	int area = 1;

	while (!dfs_q.empty()) {
		point cur_p = dfs_q.front();

		dfs_q.pop();

		for (int d = 0; d < 4; d++) {
			point mov_p = cur_p + move[d];

			if (0 <= mov_p.x && mov_p.x < n && 0 <= mov_p.y && mov_p.y < m) {
				if (maps[mov_p.y][mov_p.x] == 0) {
					dfs_q.push(mov_p);
					maps[mov_p.y][mov_p.x] = 1;
					area++;
				}
			}
		}

	}

	//print_map(maps);
	//cout << "===================================\n";
	return area; //넓이 리턴
}

int main() {

	cin.tie(NULL)->sync_with_stdio(false);

	cin >> m >> n >> k;

	int** maps = new int* [m];
	vector<int> areas;

	for (int i = 0; i < m; i++) {
		maps[i] = new int[n];
		for (int j = 0; j < n; j++) {
			maps[i][j] = 0;
		}
	}

	for (int i = 0; i < k; i++) {
		int x1, y1, x2, y2;

		cin >> x1 >> y1 >> x2 >> y2;

		for (int x = x1; x < x2; x++) {
			for (int y = y1; y < y2; y++) {
				maps[y][x] = -1;
			}
		}
	}

	for (int x = 0; x < n; x++) {
		for (int y = 0; y < m; y++) {
			if( maps[y][x] == 0 ) {
				int area = dfs(maps, x, y);
				areas.push_back(area);
			}
		}
	}

	sort(areas.begin(), areas.end());

	cout << areas.size() << "\n";
	for (int i = 0; i < areas.size(); i++) {
		cout << areas[i] << " ";
	}

	return 0;
}
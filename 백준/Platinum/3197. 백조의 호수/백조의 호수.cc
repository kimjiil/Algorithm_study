#include <iostream>
#include <queue>

using namespace std;

struct point {
	int row, col;

	point(int row, int col) : row(row), col(col) {}

	bool operator==(const point& p1) {
		if (row == p1.row && col == p1.col) {
			return true;
		}
		return false;
	}
};

void print_maps(int** maps, int row, int col) {
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			std::cout << maps[i][j];
		}
		std::cout << "\n";
	}
}

int main()
{
	cin.tie(NULL)->sync_with_stdio(false);

	int row, col;
	cin >> row >> col;

	int** maps = new int* [row];
	int** visited = new int* [row];
	vector<point> ducks;
	for (int i = 0; i < row; i++) {
		maps[i] = new int[col];
		visited[i] = new int[col];
		std::string tmp;
		cin >> tmp;
		for (int j = 0; j < col; j++) {
			visited[i][j] = 0;
			if (tmp[j] == '.') {
				maps[i][j] = 0;
			}
			else if (tmp[j] == 'X') {
				maps[i][j] = -1;
			}
			else if (tmp[j] == 'L') {
				maps[i][j] = 0;
				ducks.push_back(point(i, j));
			}
		}
	}

	//print_maps(maps, row, col);

	queue<point> bfs_q;
	queue<point> ice_q;

	// down, up, right, left
	point move[4] = { point(-1, 0), point(1, 0), point(0, 1), point(0, -1) }; 

	// 물에 인접한 모든 얼음을 찾음
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			if (maps[i][j] == 0 && visited[i][j] == 0) {
				bfs_q.push(point(i, j));
				visited[i][j] = 1;

				while (bfs_q.size() > 0) {
					point cur = bfs_q.front();
					bfs_q.pop();

					for (int m = 0; m < 4; m++) {
						int mov_i = move[m].row + cur.row;
						int mov_j = move[m].col + cur.col;
						if (0 <= mov_j && mov_j < col && 0 <= mov_i && mov_i < row) {

							// 방문하기전의 물일 경우
							if (maps[mov_i][mov_j] == 0 && visited[mov_i][mov_j] == 0) {
								bfs_q.push(point(mov_i, mov_j));
								visited[mov_i][mov_j] = 1;
							}

							// 물의 인접하면서 방문하기전의 얼음일 경우
							if (maps[mov_i][mov_j] == -1 && visited[mov_i][mov_j] == 0) {
								ice_q.push(point(mov_i, mov_j));
								visited[mov_i][mov_j] = 1;
							}
						}
					}
				}
			}
		}
	}

	/*std::cout << "==============================================\n";
	print_maps(visited, row, col);*/

	int** duck_visited = new int* [row];
	for (int i = 0; i < row; i++) {
		duck_visited[i] = new int[col];
		for (int j = 0; j < col; j++) {
			duck_visited[i][j] = 0;
		}
	}

	int day = 0;
	queue<point> next_bfs_q = queue<point>();
	queue<point> bfs_q_duck;

	point start = ducks[0];
	point end = ducks[1];
	while (true) {

		bfs_q_duck.push(ducks[0]);
		duck_visited[start.row][start.col] = 1;

		while (bfs_q_duck.size() > 0) {
			point cur = bfs_q_duck.front();
			bfs_q_duck.pop();

			if (cur == end) {
				std::cout << day << "\n";
				return 0;
			}

			for (int m = 0; m < 4; m++) {
				int mov_i = move[m].row + cur.row;
				int mov_j = move[m].col + cur.col;
				if (0 <= mov_j && mov_j < col && 0 <= mov_i && mov_i < row) {
					if (maps[mov_i][mov_j] == 0 && duck_visited[mov_i][mov_j] == 0) {
						bfs_q_duck.push(point(mov_i, mov_j));
						duck_visited[mov_i][mov_j] = 1;
					}

					if (maps[mov_i][mov_j] == -1 && duck_visited[mov_i][mov_j] == 0) {
						next_bfs_q.push(point(mov_i, mov_j));
						duck_visited[mov_i][mov_j] = 1;
					}
				}
			}
		}
		//std::cout << "================오리가 방문한 곳=====================\n";
		//print_maps(duck_visited, row, col);

		bfs_q_duck.swap(next_bfs_q);
		//bfs_q_duck = next_bfs_q;

		queue<point> next_ice_q = queue<point>();
		while (ice_q.size() > 0) {
			point cur = ice_q.front();
			maps[cur.row][cur.col] = 0; //얼음이 녹음
			ice_q.pop();
			for (int m = 0; m < 4; m++) {
				int mov_i = move[m].row + cur.row;
				int mov_j = move[m].col + cur.col;
				if (0 <= mov_j && mov_j < col && 0 <= mov_i && mov_i < row) {
					if (maps[mov_i][mov_j] == -1 && visited[mov_i][mov_j] == 0) {
						next_ice_q.push(point(mov_i, mov_j));
						visited[mov_i][mov_j] = 1;
					}
				}
			}
		}
		//std::cout << "=================얼음 상태=====================\n";
		//print_maps(maps, row, col);
		ice_q.swap(next_ice_q);
		day++;
	}
	return 0;
}
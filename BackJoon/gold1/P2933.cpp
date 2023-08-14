#include <iostream>
#include <string>
#include <queue>

using namespace std;

//global value
int ROW, COL;

int n_com;

struct point {
	int _row, _col;

	point(int _row, int _col) : _row(_row), _col(_col) {};

	bool operator==(const point& other)
	{
		if (other._col == _col && other._row == _row) {
			return true;
		}
		return false;
	}
};

template <typename T>
void print_map(T** maps) {
	//cout << "----------------------------------------------------\n";
	for (int i = 0; i < ROW; i++) {
		for (int j = 0; j < COL; j++) {
			cout << maps[i][j];
		}
		cout << "\n";
	}
}

void throw_delete(char** maps, int com, int direction) {
	int inc, start;
	if (direction == 0) {
		inc = 1;
		start = 0;
	}
	else {
		inc = -1;
		start = COL - 1;
	}
	for(int i = 0; i < COL ; i++) {
		if (maps[ROW - com][start] == 'x') {
			maps[ROW - com][start] = '.';
			return;
		}
		start = start + inc;
	}
}



int detect_cluster(char** maps)
{
	// 땅과 떨어져있는 클러스터 검사

	int** cluster_map = new int* [ROW];
	for (int i = 0; i < ROW; i++) {
		cluster_map[i] = new int[COL];
		for (int j = 0; j < COL; j++) {
			cluster_map[i][j] = 0;
		}
	}
	queue<point> q1;

	int cluster_n = 1;

	// down, up, left, right
	point move[4] = { point(1, 0), point(-1, 0), point(0, 1), point(0, -1) };

	int float_cluster = 0;

	for (int i = 0; i < ROW; i++) {
		for (int j = 0; j < COL; j++) {
			if (maps[i][j] == 'x' && cluster_map[i][j] == 0) {
				q1.push(point(i, j));
				cluster_map[i][j] = cluster_n;
				bool is_floating = true;

				while (!q1.empty()) {
					point cur = q1.front();
					q1.pop();
					if (cur._row == ROW - 1) {
						is_floating = false;;
					}
					for (int m = 0; m < 4; m++) {
						int m_row = cur._row + move[m]._row;
						int m_col = cur._col + move[m]._col;

						if (0 <= m_row && m_row < ROW && 0 <= m_col && m_col < COL) {
							if (maps[m_row][m_col] == 'x' && cluster_map[m_row][m_col] == 0) {
								q1.push(point(m_row, m_col));
								cluster_map[m_row][m_col] = cluster_n;
							}
						}
					}
				}
				if (is_floating) {
					float_cluster = cluster_n;
				}
				cluster_n++;
			}
		}
	}
	//print_map(cluster_map);

	//if (float_cluster != 0) {
	//	for (int i = ROW - 1; i >= 0; i--) {
	//		/*
	//			1. 현재 줄이 떠있는 클러스터 이면서 바로 아랫줄이 허공일 경우
	//			2. 현재 줄이 떨어지고 다시 1번 검사
	//		*/

	//		bool fall_down;
	//		bool is_float_row;
	//		int cur = i;
	//		do {
	//			fall_down = true;
	//			is_float_row = false;
	//			for (int j = 0; j < COL; j++) {
	//				// 현재 클러스터가 떠있는 클러스터고 현재 줄 바로 아래 아무것도 없을때
	//				// 떨어지는게 가능
	//				if (cluster_map[cur][j] == float_cluster) {
	//					is_float_row = true;
	//					if (cur + 1 == ROW || maps[cur + 1][j] == 'x') {
	//						fall_down = false;
	//					}
	//				}
	//			}
	//			if (fall_down && is_float_row) {
	//				for (int j = 0; j < COL; j++) {
	//					if (cluster_map[cur][j] == float_cluster) {
	//						maps[cur + 1][j] = maps[cur][j];
	//						maps[cur][j] = '.';
	//						cluster_map[cur + 1][j] = cluster_map[cur][j];
	//						cluster_map[cur][j] = 0;
	//					}
	//				}
	//			}
	//			cur++;
	//		} while (fall_down && is_float_row);

	//	}
	//}
	// 현재 클러스터가 같이 떨어져야함..

	if (float_cluster != 0) {
		bool falling = true;

		while (falling) {

			// 전체 클러스터 검사
			for (int j = 0; j < COL; j++) {
				for (int i = ROW - 1; i >= 0; i--) {
					if (cluster_map[i][j] == float_cluster) {
						if (i + 1 == ROW || maps[i + 1][j] == 'x') {
							falling = false;
						}
						break;
					}
				}
			}

			if (falling) {
				for (int i = ROW - 1; i >= 0; i--) {
					for (int j = 0; j < COL; j++) {
						if (cluster_map[i][j] == float_cluster) {
							maps[i + 1][j] = maps[i][j];
							maps[i][j] = '.';
							cluster_map[i + 1][j] = cluster_map[i][j];
							cluster_map[i][j] = 0;
						}
					}
				}
			}

		}

	}


	return 0;
}

int main() {
	cin.tie(NULL)->sync_with_stdio(false);

	cin >> ROW >> COL;

	char** maps = new char* [ROW];

	for (int i = 0; i < ROW; i++) {
		maps[i] = new char[COL];
		string temp;
		cin >> temp;
		for (int j = 0; j < COL; j++) {
			maps[i][j] = temp[j];
		}
	}
	//print_map(maps);


	// command는 항상 왼쪽->오른쪽 방향 먼저 던지고 번갈아서 던짐
	cin >> n_com;

	int* coms = new int[n_com];
	for (int i = 0; i < n_com; i++) {
		cin >> coms[i];
	}

	/*
		1. 던지고 삭제.
		2. 떨어지는 광물(cluster) 검사
		3. 해당 cluster 떨어짐
	*/

	for (int i = 0; i < n_com; i++) {
		throw_delete(maps, coms[i], i % 2);
		//print_map(maps);
		int cluster_i = detect_cluster(maps);
		//print_map(maps);
	}
	print_map(maps);

	return 0;
}
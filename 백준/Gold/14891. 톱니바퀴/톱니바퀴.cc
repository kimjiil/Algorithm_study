#include <iostream>
#include <string>
#include <vector>
#include <deque>

using namespace std;

class Saws {

public:
	vector<deque<int>> saw_v;

	void rotate(int clockwise, int idx);
	void rotate(int direct, int clockwise, int idx);
};

void Saws::rotate(int clockwise, int idx) {

	int right = saw_v[idx][2];
	int left = saw_v[idx][6];

	if (clockwise == 1) { // 시계방향
		int tmp = saw_v[idx].back();
		saw_v[idx].pop_back();

		saw_v[idx].push_front(tmp);
	}
	else if (clockwise == -1) { // 반시계 방향
		int tmp = saw_v[idx].front();
		saw_v[idx].pop_front();

		saw_v[idx].push_back(tmp);
	}
	

	// 오른쪽 방향으로
	if (idx + 1 <= 3) {
		if (right != saw_v[idx + 1][6]) {
			rotate(1, -clockwise, idx + 1);
		}
	}

	// 왼쪽 방향으로
	if (idx - 1 >= 0) {
		if (left != saw_v[idx - 1][2]) {
			rotate(-1, -clockwise, idx - 1);
		}
	}

	
}

void Saws::rotate(int direct ,int clockwise ,int idx) {

	int ns = saw_v[idx][4 - 2 * direct];

	if (clockwise == 1) { // 시계방향
		int tmp = saw_v[idx].back();
		saw_v[idx].pop_back();

		saw_v[idx].push_front(tmp);
	}
	else if (clockwise == -1) { // 반시계 방향
		int tmp = saw_v[idx].front();
		saw_v[idx].pop_front();

		saw_v[idx].push_back(tmp);
	}

	if (idx + direct >= 0 && idx + direct < 4) {
		if (ns != saw_v[idx + direct][4 + 2 * direct]) {
			rotate(direct, -clockwise, idx + direct);
		}
	}
}

int main() {

	cin.tie(NULL)->sync_with_stdio(false);

	Saws saws;

	for (int i = 0; i < 4; i++) {
		string tmp;
		cin >> tmp;

		deque<int> tmp_q;

		for (int j = 0; j < 8; j++) {
			//saws.saw[i][j] = tmp[j] - '0';// N극 : 0 , S극 : 1
			tmp_q.push_back(tmp[j] - '0');
		}

		saws.saw_v.push_back(tmp_q);
	}

	int k;

	cin >> k;

	for (int i = 0; i < k; i++) {
		int n, m; // 톱니 번호, 회전수(1: 시계 방향, -1: 반시계 방향)
		cin >> n >> m;

		saws.rotate(m, n - 1);

	}

	int score = 0;
	int ratio = 1; 
	for (int i = 0; i < 4; i++) {
		if (saws.saw_v[i][0] == 1) {
			score += (ratio);
		}
		ratio *= 2;
	}

	cout << score;
	
	return 0;
}
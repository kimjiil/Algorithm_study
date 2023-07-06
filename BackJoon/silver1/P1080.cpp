#include <iostream>
#include <vector>
#include <string>

using namespace std;

int matrix_change(vector<vector<int>> &mA, vector<vector<int>> &mB, int x, int y) {

		// 서로 보수의 관계면 바꿈
	if (mA[y - 1][x - 1] == mB[y - 1][x - 1]) {
		return 0;
	}

	for (int j = -1; j < 2; j++) {
		for (int i = -1; i < 2; i++) {
			mA[y + j][x + i] = 1 - mA[y + j][x + i];
		}
	}
	return 1;
}
int is_equal(vector<vector<int>>& mA, vector<vector<int>>& mB) {
	int n, m;
	n = mA.size(); // 18
	m = mA[0].size(); // 3
	for (int y = 0; y < n; y++) {
		for (int x = 0; x < m; x++) {
			if (mA[y][x] != mB[y][x]) {
				return false;
			}
		}
	}
	return true;
}
int matrix_func(vector<vector<int>> &mA, vector<vector<int>> &mB) {
	int n, m;
	n = mA.size(); // 18
	m = mA[0].size(); // 3
	int count = 0;
	for (int y = 1; y < n - 1; y++) {
		for (int x = 1; x < m - 1; x++) {
			count += matrix_change(mA, mB, x, y);
		}
	}
	if (is_equal(mA, mB)) {
		return count;
	}
	else {
		return -1;
	}
}

int main()
{
	cin.tie(NULL)->sync_with_stdio(false);
	int N, M;

	cin >> N >> M;

	vector<vector<vector<int>>> matrix;
	vector<vector<int>> A;
	vector<int> temp;
	for (int k = 0; k < 2; k++) {
		for (int i = 0; i < N; i++) {
			string s;
			cin >> s;
			for (char& c : s) {
				temp.push_back(c - '0');
			}
			A.push_back(temp);
			temp.clear();
		}
		matrix.push_back(A);
		A.clear();
	}

	cout << matrix_func(matrix[0], matrix[1]) << "\n";
}

// 3x3변환에서 독립성있는 부분은 왼쪽 상위 끝 모서리 부분만 비교해서 바꾸면 최소 변환수가 나옴
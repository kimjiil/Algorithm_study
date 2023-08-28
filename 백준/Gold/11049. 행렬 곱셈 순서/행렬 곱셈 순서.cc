#include <iostream>
#include <vector>
#include <climits>
#include <iomanip>
#include <string>

#define ULL unsigned long long int

using namespace std;

struct mat {
	int row, col;

	mat(int row, int col) : row(row), col(col) {}
};

template <typename T>
void myprint(T** p, int n) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			string tmp = to_string(p[i][j]);
			if (tmp.length() > 10) {
				cout << setw(10) <<"X" <<" ";
			}
			else {
				cout << setw(10) << tmp << " ";
			}
		}
		cout << "\n";
	}
}

ULL solution(const vector<mat>& mat_list) {

	int n_mat = mat_list.size();
	ULL** dp = new ULL * [n_mat];
	for (int i = 0; i < n_mat; i++) {
		dp[i] = new ULL[n_mat];
		for (int j = 0; j < n_mat; j++) {
			dp[i][j] = ULLONG_MAX;
		}
	}

	for (int k = 0; k < n_mat; k++) {
		for (int i = 0; i < n_mat - k; i++) {
			if (k == 0) {
				dp[i][i + k] = 0;
			}
			for (int j = i; j < i + k; j++) {
				ULL mat_cost = mat_list[i].row * mat_list[j + 1].row * mat_list[i + k].col;
				dp[i][i + k] = min(dp[i][i+k], dp[i][j] + dp[j + 1][i + k] + mat_cost);

				//cout << i << " " << j << " " << i + k << " " << dp[i][i + k] << "\n";
			}
		}
	}
	//myprint(dp, n_mat);
	return dp[0][n_mat-1];
}

int main() {

	cin.tie(NULL)->sync_with_stdio(false);
	
	int n_mat;
	cin >> n_mat;
	vector<mat> mat_list;

	for (int i = 0; i < n_mat; i++) {
		int t_r, t_c;
		cin >> t_r >> t_c;
		mat_list.push_back(mat(t_r, t_c));
	}

	cout << solution(mat_list) << "\n";

	return 0;
}
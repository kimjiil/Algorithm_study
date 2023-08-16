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

template <typename T,typename T2>
void myprint(T** p, T2** A, int n) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			string tmp = to_string(p[i][j]);
			if (tmp.length() > 10) {
				cout << setw(10) <<"X" <<" " << setw(3) << to_string(A[i][j]);
			}
			else {
				cout << setw(10) << tmp << " " << setw(3) << to_string(A[i][j]);
			}
		}
		cout << "\n";
	}
}

// 사각부등식 성립안해서 크눅스 성립안함
ULL solution_knuth(const vector<mat>& mat_list) {

	int n_mat = mat_list.size();
	ULL** dp = new ULL * [n_mat];
	int** A = new int* [n_mat];
	for (int i = 0; i < n_mat; i++) {
		dp[i] = new ULL[n_mat];
		A[i] = new int[n_mat];
		for (int j = 0; j < n_mat; j++) {
			dp[i][j] = ULLONG_MAX;

			if (i == j) {
				A[i][j] = i;
			}
			else {
				A[i][j] = 0;
			}
		}
	}

	for (int k = 0; k < n_mat; k++) {
		for (int i = 0; i < n_mat - k; i++) {
			if (k == 0) {
				dp[i][i + k] = 0;
			}
			else {
				for (int j = A[i][i + k - 1]; j < min(A[i + 1][i + k] + 1, i + k) ; j++) {
					ULL mat_cost = mat_list[i].row * mat_list[j + 1].row * mat_list[i + k].col;
					if (dp[i][i + k] > dp[i][j] + dp[j + 1][i + k] + mat_cost) {
						dp[i][i + k] = dp[i][j] + dp[j + 1][i + k] + mat_cost;
						A[i][i + k] = j;
					}
					//dp[i][i + k] = min(dp[i][i + k], dp[i][j] + dp[j + 1][i + k] + mat_cost);

					//cout << i << " " << j << " " << i + k << " " << dp[i][i + k] << "\n";
				}
			}
		}
	}
	myprint(dp, A, n_mat);
	return dp[0][n_mat - 1];
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

	//cout << solution_knuth(mat_list) << "\n";
	cout << solution(mat_list) << "\n";

	return 0;
}
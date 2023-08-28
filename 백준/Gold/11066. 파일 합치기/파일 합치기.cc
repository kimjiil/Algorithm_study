#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

template <typename T, typename T2>
void print_dp(T** dp, T2** A ,int n) {
	cout << "----------------------------------------\n";
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			string temp = to_string(dp[i][j]);
			string t = to_string(A[i][j]);
			if (temp.length() <= 5) {
				cout << setw(5) << temp << setw(3) <<t;
			}
			else {
				cout << "       X";
			}
		}
		cout << "\n";

	}
}

int recur_met(int* files, int* accum, int start_idx, int end_idx) {

	/*for (int i = start_idx; i <= end_idx; i++) {
		cout << files[i] << " ";
	}
	cout << "\n";*/
	if (end_idx == start_idx) {
		return 0;
	}
	
	int cost = INT32_MAX;
	
	for (int split = start_idx; split < end_idx; split++) {

		int left_cost = recur_met(files, accum, start_idx, split);
		int right_cost = recur_met(files, accum ,split + 1, end_idx);
		int tmp_cost = left_cost + right_cost + (accum[end_idx + 1] - accum[start_idx]);
		if (cost > tmp_cost) {
			cost = tmp_cost;
		}
	}

	return cost;
}



int dp_met(int* files, int* accum, int n_file) {

	int** dp = new int* [n_file];
	int** A = new int* [n_file];
	for (int i = 0; i < n_file; i++) {
		dp[i] = new int[n_file];
		A[i] = new int[n_file];
		for (int j = 0; j < n_file; j++) {
			dp[i][j] = INT32_MAX;
			if (i == j) {
				A[i][j] = i;
			}
			else {
				A[i][j] = 0;
			}
		}
	}


	for (int k = 0; k <= n_file; k++) { // 길이
		for (int i = 0; i < n_file - k; i++) { // 시작 지점
			if (k == 0) {
				dp[i][i + k] = 0;
			}
			else {
				for (int j = A[i][i + k - 1]; j < min(A[i + 1][i + k] + 1, i+ k); j++) { // split 지점
					int tmp = dp[i][j] + dp[j + 1][i + k] + accum[i + k + 1] - accum[i];
					//dp[i][i+k] = min(dp[i][i+k], tmp);
					if (dp[i][i + k] > tmp) {
						dp[i][i + k] = tmp;
						A[i][i + k] = j;
					}
					//cout << i << " " << j << " " << k + i << " " << dp[i][j] + dp[j + 1][i + k] + accum[i + k + 1] - accum[i] << "\n";
				}
			}
		}
		//print_dp(dp, A, n_file);
	}

	return dp[0][n_file - 1];
}

int solution(int* files, int n_file) {
	int* accum_list = new int[n_file + 1];
	accum_list[0] = 0;
	for (int i = 1; i < n_file + 1; i++) {
		accum_list[i] = accum_list[i - 1] + files[i - 1];
	}
	//int tmp = recur_met(files, accum_list, 0, n_file - 1);
	int tmp = dp_met(files, accum_list, n_file);
	return tmp;
}

int main() {

	cin.tie(NULL)->sync_with_stdio(false);

	int n_task;
	cin >> n_task;

	for (int t = 0; t < n_task; t++) {
		int n_file;
		cin >> n_file;
		int* files = new int[n_file];
		for (int i = 0; i < n_file; i++) {
			cin >> files[i];
		}
		
		cout << solution(files, n_file) << "\n";
	}

	return 0;
}
#include <iostream>

#define int_type unsigned long long int

using namespace std;

void print_mat(int_type** mat, int_type n) {
	for (int_type i = 0; i < n; i++) {
		for (int_type j = 0; j < n; j++) {
			cout << mat[i][j] << " ";
		}
		cout << "\n";
	}
}

int_type** mat_mul(int_type** mat1, int_type** mat2, int_type n) {
	int_type** result_mat = new int_type * [n];
	for (int_type i = 0; i < n; i++) {
		result_mat[i] = new int_type[n];
		for (int_type j = 0; j < n; j++) {
			result_mat[i][j] = 0;
			for (int_type k = 0; k < n; k++) {
				result_mat[i][j] = (result_mat[i][j] + mat1[i][k] * mat2[k][j]) % 1000 ;
			}
		}
	}
	return result_mat;
}

int_type** mat_pow(int_type** mat, int_type p, int_type n) {
	int_type** res_mat;

	if (p == 0) {
		res_mat = new int_type * [n];
		for (int_type i = 0; i < n; i++) {
			res_mat[i] = new int_type[n];
			for (int_type j = 0; j < n; j++) {
				if (i == j) {
					res_mat[i][j] = 1;
				}
				else {
					res_mat[i][j] = 0;
				}
			}
		}
		return res_mat;
	}
	int_type** temp = mat_pow(mat, p / 2, n);
	res_mat = mat_mul(temp, temp, n);
	if (p % 2 == 0) {
		return res_mat;
	}
	else {
		int_type**tmp = mat_mul(res_mat, mat, n);
		return tmp;
	}
}

int main() {

	cin.tie(NULL)->sync_with_stdio(false);

	int_type n, p;

	cin >> n >> p;

	int_type** mat = new int_type * [n];
	for (int_type i = 0; i < n; i++) {
		mat[i] = new int_type[n];
		for (int_type j = 0; j < n; j++) {
			cin >> mat[i][j];
		}
	}

	int_type** res_mat = mat_pow(mat, p, n);
	print_mat(res_mat, n);

	return 0;
}
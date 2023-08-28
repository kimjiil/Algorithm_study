
#include <iostream>

using namespace std;

#define ULLI unsigned long long int
#define mod_n (ULLI)1000000

void mat_mul(ULLI (*res)[2], ULLI(*mat1)[2], ULLI(*mat2)[2]) {
	
	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 2; j++) {
			res[i][j] = 0;

			for (int k = 0; k < 2; k++) {
				res[i][j] = (res[i][j] + mat1[i][k] * mat2[k][j]) % mod_n;
			}
		}
	}
}

void mat_pow(ULLI(*res)[2], ULLI(*mat)[2], ULLI p) {
	if (p == 1) {
		for (int i = 0; i < 2; i++) {
			for (int j = 0; j < 2; j++) {
				res[i][j] = mat[i][j];
			}
		}
		return;
	}
	ULLI temp[2][2];
		
	mat_pow(temp, mat, p / 2);
	if (p % 2 == 0) {
		mat_mul(res, temp, temp);
		return;
	}
	else {
		ULLI tmp[2][2];
		mat_mul(tmp, temp, temp);
		mat_mul(res, tmp, mat);
		return;
	}
}

int main() {
	cin.tie(NULL)->sync_with_stdio(false);

	ULLI n;
	cin >> n;

	ULLI fib_mat[2][2] = {1, 1, 1, 0};

	ULLI res_mat[2][2];
	mat_pow(res_mat, fib_mat, n);

	std::cout << res_mat[0][1] << "\n";

	return 0;
}
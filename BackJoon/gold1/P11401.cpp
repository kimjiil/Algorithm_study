#include <iostream>
#include <math.h>

#define int_type unsigned long long int
#define bign (int_type)1000000007
using namespace std;

int_type my_pow(int_type a, int_type p) {
	if (p == 0) {
		return 1;
	}
	int_type result = 1;
	int_type temp = my_pow(a, p / 2);
	result = (result * temp * temp) % bign;
	if (p % 2 == 0) {
		return result;
	}
	else {
		result = (result * a) % bign;
		return result;
	}
}
// 303317497

int main() {
	cin.tie(NULL)->sync_with_stdio(false);
	int n, k;
	cin >> n >> k;

	k = min(k, n - k);

	int_type a = 1;
	int_type b = 1;

	for (int i = 1; i <= k; i++) {
		a = (a * (n - i + 1)) % bign;
		b = (b * i) % bign;
	}

	int_type temp = my_pow(b, bign - 2);
	int_type result = (a * temp) % bign;
	std::cout << result << "\n";
	return 0;
}
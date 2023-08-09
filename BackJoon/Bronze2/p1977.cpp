#include <iostream>
#include <math.h>

using namespace std;

int main()
{
	cin.tie(NULL)->sync_with_stdio(false);

	int N, M;
	cin >> N >> M;

	int left = int(ceil(pow(N, 0.5)));
	int right = int(floor(pow(M, 0.5)));
	int sum = 0;
	for (int i = left; i <= right; i++) {
		sum = sum + pow(i, 2);
	}
	if (sum == 0) {
		cout << -1;
	}
	else {
		cout << sum << "\n" << pow(left, 2) << endl;
	}

	return 0;
}
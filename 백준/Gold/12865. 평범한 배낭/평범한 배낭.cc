#include <iostream>

using namespace std;

int main()
{
	cin.tie(NULL)->sync_with_stdio(false);

	int n, k;

	cin >> n >> k;

	int dp[100001] = {};

	for (int i = 0; i < n; i++) {
		int w, v;
		cin >> w >> v;
		for (int j = k; j > 0; j--) {
			if (j >= w) {
				dp[j] = max(dp[j], dp[j - w] + v);
			}
		}
	}
	std::cout << dp[k] << std::endl;

	return 0;
}
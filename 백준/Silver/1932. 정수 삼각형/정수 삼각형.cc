#include <iostream>

using namespace std;

int main() {
    cin.tie(NULL)->sync_with_stdio(false);

    int n;
    int tri[500] = { 0, };
    int dp[500][500] = { 0, };
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            cin >> tri[j];
            dp[i][j] = tri[j];
        }

        
        if (i != 0) {
            for (int j = 0; j <= i; j++) {
                for (int k = j; k >= j - 1; k--) {
                    if (j >= 0) {
                        dp[i][j] = max(dp[i - 1][k] + tri[j], dp[i][j]);
                    }
                }
            }
        }
    }
    int max_value = 0;
    for (int i = 0; i < n; i++) {
        if (max_value < dp[n - 1][i]) {
            max_value = dp[n - 1][i];
        }
    }
   
    cout << max_value;
    return 0;
}
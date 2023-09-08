#include <iostream>

using namespace std;
int dp[1000001] = { 0, };

int main()
{
    cin.tie(NULL)->sync_with_stdio(false);
    int N; // 1,000,000
    cin >> N;
    
    
    for (int i = N - 1; i > 0; i--) {
        int dp3= 1000001, dp2= 1000001, dpm;
        dpm = dp[i + 1] + 1;
        if (i * 2 <= N) {
            dp2 = dp[i * 2] + 1;
        }
        if (i * 3 <= N) {
            dp3 = dp[i * 3] + 1;
        }
        dp[i] = min(dpm, min(dp3, dp2));
    }
    cout << dp[1];
    return 0;
}
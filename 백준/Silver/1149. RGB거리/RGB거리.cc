#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    cin.tie(NULL)->sync_with_stdio(false);
    
    int n;
    cin >> n;
    int rgb[3];
    int dp[3];
    int tmp[3];
    for(int i = 0 ; i < n ; i ++) {
        for(int j = 0 ; j < 3 ; j ++) {
            cin >> rgb[j]; //현재값
            if(i == 0) {
                dp[j] = rgb[j];
            }
        }
        
        if(i != 0) {
            for(int j = 0; j < 3; j++) {
                tmp[j] = dp[j];
            }
            dp[0] = min(tmp[1], tmp[2]) + rgb[0];
            dp[1] = min(tmp[0], tmp[2]) + rgb[1];
            dp[2] = min(tmp[0], tmp[1]) + rgb[2];
        }
    }
    
    int min_value = 1000 * 1000 + 1;
    for(int j = 0 ; j < 3 ; j++) {
        if (min_value > dp[j]) {
            min_value = dp[j];
        }
    }
    
    cout << min_value;
    
    return 0;
}
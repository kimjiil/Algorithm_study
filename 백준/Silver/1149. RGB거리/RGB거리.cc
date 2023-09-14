#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    cin.tie(NULL)->sync_with_stdio(false);
    
    int n;
    cin >> n;
    int ** rgb = new int*[n];
    // int ** dp = new int[n];
    for(int i = 0 ; i < n ; i ++) {
        rgb[i] = new int[3];
        // dp[i] = new int[3];
        for(int j = 0 ; j < 3 ; j ++) {
            cin >> rgb[i][j];
            // dp[i][j] =
        }
    }
    for(int i = 1 ; i < n ; i++) {
        rgb[i][0] = min(rgb[i-1][1], rgb[i-1][2]) + rgb[i][0];
        rgb[i][1] = min(rgb[i-1][0], rgb[i-1][2]) + rgb[i][1];
        rgb[i][2] = min(rgb[i-1][0], rgb[i-1][1]) + rgb[i][2];
    }
    
    int min_value = 1000 * 1000 + 1;
    for(int j = 0 ; j < 3 ; j++) {
        if (min_value > rgb[n-1][j]) {
            min_value = rgb[n-1][j];
        }
    }
    
    cout << min_value;
    
    return 0;
}
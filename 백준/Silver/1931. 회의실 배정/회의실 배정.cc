#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;


int main() {
    cin.tie(NULL)->sync_with_stdio(false);

    int n;
    
    priority_queue < pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    cin >> n;

    for (int i = 0; i < n; i++) {
        int start, end;
        cin >> start >> end;
        pq.push(make_pair(end, start));
    }

    int prev_end = 0;

    int t = 0;

    for (int i = 0; i < n; i++) {
        pair<int, int> cur_time = pq.top();

        int cur_start = cur_time.second;
        int cur_end = cur_time.first;

        if (prev_end <= cur_start) {
            prev_end = cur_end;
            t++;
        }

        pq.pop();
    }

    cout << t;
    return 0;
}
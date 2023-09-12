#include <iostream>
#include <queue>

using namespace std;
int visited[100001] = { 0, };

#define max_len 100000
int main() {
    cin.tie(NULL)->sync_with_stdio(false);

    int n, k;
    int answer;
    cin >> n >> k;

    queue<int> q;
    
    q.push(n);
    visited[n] = 1;
    while (!q.empty()) {
        int cur = q.front();
        q.pop();

        if (cur == k) {
            break;
        }

        if (2 * cur <= max_len && visited[2 * cur] == 0) {
            q.push(2 * cur);
            visited[2 * cur] = visited[cur] + 1;
        }
        if (cur + 1 <= max_len && visited[cur + 1] == 0) {
            q.push(cur + 1);
            visited[cur + 1] = visited[cur] + 1;
        }
        if (cur - 1 >= 0 && visited[cur - 1] == 0) {
            q.push(cur - 1);
            visited[cur - 1] = visited[cur] + 1;
        }
    }

    cout << visited[k] - 1;
    return 0;
}
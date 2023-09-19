#include <iostream>
#include <queue>

using namespace std;

struct point {
    int x, y;
    int d;

    point(int x, int y) : x(x), y(y), d(0) {

    }

    point(int x, int y, int d) : x(x), y(y), d(d) {

    }

    bool operator==(point& other) {
        if (x == other.x && y == other.y) {
            return true;
        }
        return false;
    }
    
    point operator+(point& other) {
        return point(x + other.x, y + other.y, d + 1);
    }
};

int solution() {

    int n; // 체스판 변의 길이
    cin >> n;

    int** visited = new int*[n];
    for (int i = 0; i < n; i++) {
        visited[i] = new int[n];
        for (int j = 0; j < n; j++) {
            visited[i][j] = 0;
        }
    }

    int s_x, s_y; // 시작 지점
    cin >> s_x >> s_y;
    int t_x, t_y; // 도착 지점
    cin >> t_x >> t_y;

    queue<point> q;

    point end(t_x, t_y);
    q.push(point(s_x, s_y, 0));
    visited[s_x][s_y] = 1;

    point move_point[8] = { point(1, 2), point(2, 1),
                            point(-1, -2), point(-2, -1),
                            point(-1, 2), point(-2, 1),
                            point(1, -2), point(2, -1)};

    
    while (!q.empty()) {
        point cur = q.front();
        q.pop();

        for (int m = 0; m < 8; m++) {
            point m_p = cur + move_point[m];

            if (0 <= m_p.x && m_p.x < n && 0 <= m_p.y && m_p.y < n && visited[m_p.x][m_p.y] == 0) {
                q.push(m_p);
                visited[m_p.x][m_p.y] = 1;
                if (m_p == end) {
                    return m_p.d;
                }
            }

        }
    }

    return 0;
}

int main() {
    cin.tie(NULL)->sync_with_stdio(false);

    int n_t;

    cin >> n_t;

    for (int tc = 0; tc < n_t; tc++) {
        int sol = solution();
        cout << sol << "\n";
    }
    return 0;
}
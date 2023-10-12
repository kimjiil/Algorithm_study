#include <iostream>
#include <queue>
using namespace std;

int N;
int** maps;

struct point {
    int col, row;

    point(int row, int col) : row(row), col(col) {};
};

int dfs(int deeper) {
    bool visited[100][100] = { false, };
    queue<point> q;

    point dir[4] = { point(1, 0), point(-1, 0) , point(0, 1) ,point(0, -1) };

    int region = 0;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (!visited[i][j] && maps[i][j] > deeper) {
                q.push(point(i, j));
                visited[i][j] = true;

                while (!q.empty()) {
                    point cur = q.front();
                    q.pop();

                    for (int d = 0; d < 4; d++) {
                        int _row = cur.row + dir[d].row;
                        int _col = cur.col + dir[d].col;

                        if (0 <= _row && _row < N && 0 <= _col && _col < N && maps[_row][_col] > deeper
                            && !visited[_row][_col]) {
                            q.push(point(_row, _col));
                            visited[_row][_col] = true;
                        }
                    }
                }

                region++;
            }
        }
    }
    return region;
}

int main() {
    cin.tie(NULL)->sync_with_stdio(false);
    // N <= 100
    cin >> N;
    maps = new int* [N];

    int min_n = 100, max_n = 1;
    for (int i = 0; i < N; i++) {
        maps[i] = new int[N];
        for (int j = 0; j < N; j++) {
            cin >> maps[i][j];
            if (min_n > maps[i][j]) min_n = maps[i][j];
            if (max_n < maps[i][j]) max_n = maps[i][j];
        }
    }
    int max_region = 1;
    for (int n = min_n; n < max_n; n++) {
        int reg = dfs(n);
        if (reg > max_region) max_region = reg;
    }

    cout << max_region;
    return 0;
}
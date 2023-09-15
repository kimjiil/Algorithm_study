#include <iostream>
#include <vector>

using namespace std;

int h, w;

void print_map(int** map) {
    
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            cout << map[i][j] << " ";
        }
        cout << "\n";
    }
}

int main() {
    cin.tie(NULL)->sync_with_stdio(false);

    cin >> h >> w;

    int** chess_table = new int*[h];
    for (int i = 0; i < h; i++) {
        chess_table[i] = new int[w];
        for (int j = 0; j < w; j++) {
            chess_table[i][j] = 0;
        }
    }
    int safe_point = h * w;
    // 0 : queen / 1 : knight / 2 : pawn
    vector<vector<pair<int, int>>> chess;

    for (int i = 0; i < 3; i++) {
        int n;
        cin >> n;
        vector<pair<int, int>> tmp;
        for (int j = 0; j < n; j++) {
            int y, x;
            cin >> y >> x;
            tmp.push_back(make_pair(x - 1, y - 1));
            chess_table[y - 1][x - 1] = i + 1;
            safe_point--;
        }
        chess.push_back(tmp);
    }

    int m_x[2] = { -1, 1 };

    
    // queen  
    for (int i = 0; i < chess[0].size(); i++) {
        int q_x, q_y;
        q_x = chess[0][i].first;
        q_y = chess[0][i].second;

        for (int m_x = -1; m_x <= 1; m_x ++) {
            for (int m_y = -1; m_y <= 1; m_y ++) {
                if (m_x != 0 || m_y != 0) {
                    int _x, _y;
                    _x = q_x + m_x;
                    _y = q_y + m_y;
                    while (0 <= _x && _x < w && 0 <= _y && _y < h && chess_table[_y][_x] <= 1) {
                        if (chess_table[_y][_x] == 0) {
                            safe_point--;
                        }
                        chess_table[_y][_x] = 1;
                        _x += m_x;
                        _y += m_y;

                    }
                }
            }
        }
    }
    // knight 
    for (int i = 0; i < chess[1].size(); i++) {
        int q_x, q_y;
        q_x = chess[1][i].first;
        q_y = chess[1][i].second;

        for (int m_x = -1; m_x <= 1; m_x += 2) {
            for (int m_y = -1; m_y <= 1; m_y += 2) {
                for (int c = 1; c <= 2; c++) {
                    int _x, _y;

                    _x = q_x + m_x * c;
                    _y = q_y + m_y * (3 - c);

                    if (0 <= _x && _x < w && 0 <= _y && _y < h && chess_table[_y][_x] == 0) {
                        chess_table[_y][_x] = 2;
                        safe_point--;
                    }
                }
                
            }
        }
    }


    //print_map(chess_table);
    cout << safe_point;
    return 0;
}
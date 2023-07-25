# 레이저 통신

import sys

input = sys.stdin.readline

def solution():
    col, row = map(int, input().split())
    maps = []
    target = []
    for i in range(row):
        maps.append(list(input().replace("\n", '')))
        for j in range(col):
            if maps[i][j] == 'C':
                target.append((i, j))

    start, end = target

    q = [(*start, 0), (*start, 1), (*start, 2), (*start, 3)]

    dp = [[[0, 0, 0, 0] for _ in range(col)] for _ in range(row)]

    dp[start[0]][start[1]][0] = 1
    dp[start[0]][start[1]][1] = 1
    dp[start[0]][start[1]][2] = 1
    dp[start[0]][start[1]][3] = 1


    while q:
        i, j, d_t = q.pop(0)

        for d_i, m in enumerate([(1, 0), (0, 1), (-1, 0), (0, -1)]): #down, right, up, left
            m_i = i + m[0]
            m_j = j + m[1]

            if 0 <= m_i and m_i < row and 0 <= m_j and m_j < col:
                if maps[m_i][m_j] != '*':
                    if d_t % 2 == d_i % 2: #같은 방향
                        if dp[m_i][m_j][d_i] == 0:
                            dp[m_i][m_j][d_i] = dp[i][j][d_t]
                            q.append((m_i, m_j, d_i))
                        else:
                            if dp[m_i][m_j][d_i] > dp[i][j][d_t]:
                                dp[m_i][m_j][d_i] = dp[i][j][d_t]
                                q.append((m_i, m_j, d_i))
                    elif d_t % 2 != d_i % 2: #다른 방향
                        if dp[m_i][m_j][d_i] == 0:
                            dp[m_i][m_j][d_i] = dp[i][j][d_t] + 1
                            q.append((m_i, m_j, d_i))
                        else:
                            if dp[m_i][m_j][d_i] > dp[i][j][d_t] + 1:
                                dp[m_i][m_j][d_i] = dp[i][j][d_t] + 1
                                q.append((m_i, m_j, d_i))

    min_value =214700000
    for i in dp[end[0]][end[1]]:
        if i != 0 and min_value > i:
            min_value = i

    print(min_value - 1)

solution()
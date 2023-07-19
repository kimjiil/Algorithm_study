# 백조의 호수
'''
bfs 탐색으로
1번 오리 큐
2번 오리큐 번갈아 가면서 탐색하다가 1번과 2번이 인접하면 end

'''
from collections import deque
import sys
input = sys.stdin.readline

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def solution():
    def swan_dfs():
        while swan_q:
            i, j = swan_q.popleft()

            if (i, j) == (i_2, j_2):
                return True  # 두번쨰 오리를 발견하면 stop

            for m in move:
                m_i = i + m[0]
                m_j = j + m[1]

                if m_i < row and m_i >= 0 and m_j < col and m_j >= 0:
                    if swan_visited[m_i][m_j] == 0 and maps[m_i][m_j] == '.':
                        swan_visited[m_i][m_j] = 1
                        swan_q.append([m_i, m_j])

                    if maps[m_i][m_j] == 'X' and swan_visited[m_i][m_j] == 0:
                        new_swan_q.append([m_i, m_j])
                        swan_visited[m_i][m_j] = 1

        return False

    def water_dfs():
        ice = deque()
        while water_q:
            i, j = water_q.popleft()

            for m in move:
                m_i, m_j = i + m[0], j + m[1]
                if m_i < row and m_i >= 0 and m_j < col and m_j >= 0:
                    if maps[m_i][m_j] == 'X':
                        ice.append([m_i, m_j])
                        ice_visited[m_i][m_j] = 1
                        maps[m_i][m_j] = '.'

        return ice

    row, col = map(int, input().split())
    maps = []
    ice_visited = [[0] * col for _ in range(row)]
    swan_visited = [[0] * col for _ in range(row)]
    swan = []
    water_q = deque()

    for i in range(row):
        maps.append(list(input().replace('\n', '')))
        for j in range(col):
            if maps[i][j] == 'L':
                swan.append([i, j])
                water_q.append([i, j])
                maps[i][j] = '.'
            if maps[i][j] == '.':
                water_q.append([i, j])

    if len(swan) < 2:
        return 0

    i_1, j_1 = swan[0]
    i_2, j_2 = swan[1]
    swan_q = deque([])
    swan_q.append([i_1, j_1])
    swan_visited[i_1][j_1] = 1

    day = 0
    while True:
        new_swan_q = deque()
        if swan_dfs():
            return day
        day += 1
        water_q = water_dfs()
        swan_q = new_swan_q


def solution1():
    def adj_ori(i, j, maps, row, col):
        for _i, _j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            n_i = _i + i
            n_j = _j + j
            if n_i >= 0 and row > n_i and n_j >= 0 and col > n_j:
                if maps[n_i][n_j] + maps[i][j] == 3:  # 서로 맞닿았으면
                    return True

    row, col = map(int, input().split())
    maps = [[0 for _ in range(col)] for _ in range(row)]

    ori_num = 1
    q = [deque([]), deque([])]
    ice_q = [deque([]), deque([])]
    for i in range(row):
        row_map = list(input().replace('\n', ''))
        for j in range(col):
            if row_map[j] == 'L':
                maps[i][j] = ori_num
                q[ori_num - 1].append((i, j))
                ori_num += 1
            if row_map[j] == 'X':
                maps[i][j] = -1

    for ori_i in range(2):
        while len(q[ori_i]) > 0:
            cur_i, cur_j = q[ori_i].popleft()

            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                n_i = cur_i + i
                n_j = cur_j + j
                if n_i >= 0 and row > n_i and n_j >= 0 and col > n_j:
                    if maps[n_i][n_j] == 0:
                        q[ori_i].append((n_i, n_j))
                        maps[n_i][n_j] = ori_i + 1
                    elif maps[n_i][n_j] == -1:
                        ice_q[ori_i].append((n_i, n_j))

    day = 0
    while len(ice_q[0]) + len(ice_q[1]) > 0:
        for ori_i in range(2):
            temp = deque([])
            for i, j in ice_q[ori_i]:
                maps[i][j] = ori_i + 1 # 오리 번호
                if adj_ori(i, j, maps, row, col):
                    return day + 1

            while len(ice_q[ori_i]) > 0:
                cur_i, cur_j = ice_q[ori_i].popleft()
                for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    n_i = cur_i + i
                    n_j = cur_j + j
                    if n_i >= 0 and row > n_i and n_j >= 0 and col > n_j:
                        if maps[n_i][n_j] == -1:
                            temp.append((n_i, n_j))
            ice_q[ori_i] = temp
        day += 1
    return day

if __name__ == '__main__':
    day = solution()
    print(day)
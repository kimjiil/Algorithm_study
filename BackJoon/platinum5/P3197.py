# 백조의 호수
'''
bfs 탐색으로
1번 오리 큐
2번 오리큐 번갈아 가면서 탐색하다가 1번과 2번이 인접하면 end

'''

import sys
input = sys.stdin.readline

def adj_ori(i, j, maps, row, col):
    for _i, _j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        n_i = _i + i
        n_j = _j + j
        if n_i >= 0 and row > n_i and n_j >= 0 and col > n_j:
            if maps[n_i][n_j] + maps[i][j] == 3:  # 서로 맞닿았으면
                return True

def solution():
    row, col = map(int, input().split())
    maps = [[0 for _ in range(col)] for _ in range(row)]

    ori_num = 1
    q = [[], []]
    ice_q = [[], []]
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
            cur_i, cur_j = q[ori_i].pop(0)

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
            temp = []
            for i, j in ice_q[ori_i]:
                maps[i][j] = ori_i + 1 # 오리 번호
                if adj_ori(i, j, maps, row, col):
                    return day + 1

            while len(ice_q[ori_i]) > 0:
                cur_i, cur_j = ice_q[ori_i].pop(0)
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
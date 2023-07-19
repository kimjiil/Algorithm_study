# 미네랄
'''
1번째 왼쪽 -> 오른쪽
2번쨰 왼쪽 <- 오른쪽
막대에 맞으면 미네랄은 파괴되고
클러스터의 모양은 떨어지는 동안에 변하지 않는다.
클러스터의 최첨단이 땅에 닿아야 낙하를 멈춤

1. 던진다.
2. 땅에서 떨어진 클러스터가 있는지 조사한다.
3. 낙하
'''

import sys
from collections import deque

input = sys.stdin.readline

def throwing(grave_map, throw_direct, h):
    # for i in grave_map[8 - h]:
    col_n = len(grave_map[0])
    row_n = len(grave_map)
    idx = [i for i in range(col_n)]
    for i in idx[::throw_direct]:
        if grave_map[row_n-h][i] == 'x':
            grave_map[row_n-h][i] = '.'
            return

def bfs(point, grave_map, group):
    col = len(grave_map[0])
    row = len(grave_map)
    q = deque([point])
    i, j = point
    cluster_i = group[i][j]

    is_floating = True
    while q:
        i, j = q.popleft()

        for m in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            m_i = i + m[0]
            m_j = j + m[1]
            if row > m_i and m_i >= 0 and col > m_j and m_j >=0:
                if grave_map[m_i][m_j] == 'x' and group[m_i][m_j] != cluster_i:
                    group[m_i][m_j] = cluster_i
                    q.append((m_i, m_j))

                    if m_i == row - 1:
                        is_floating = False

    return is_floating, cluster_i

def falling(grave_map, group, idx):
    row = len(grave_map)
    col = len(grave_map[0])
    is_float = True
    while is_float:
        for i in range(row - 1, -1, -1):
            for j in range(col):

                if group[i][j] == idx:
                    group[i+1][j] = idx
                    group[i][j] = 0
                    grave_map[i][j] = '.'
                    grave_map[i + 1][j] = 'x'

                    if i + 1 == row - 1: #땅바닥에 닿은 경우
                        is_float = False

                    # 다른 클러스터에 닿은 경우
                    if i + 2 < row and group[i+2][j] != idx and group[i+2][j] > 0:
                        is_float = False


def find_cluster(grave_map):
    row = len(grave_map)
    col = len(grave_map[0])

    group = [[0] * col for _ in range(row)]
    cnt = 1

    falling_q = deque()
    for i in range(row):
        for j in range(col):
            if grave_map[i][j] == 'x' and group[i][j] == 0:
                group[i][j] = cnt
                cnt += 1
                is_float, cluster_i = bfs((i, j), grave_map, group)

                if is_float:
                    falling_q.append(cluster_i)


    while falling_q:
        falling_cluster = falling_q.popleft()
        falling(grave_map, group, falling_cluster)

def solution():
    row, col = map(int, input().split())

    grave_map = []
    for i in range(row):
        grave_map.append(list(input().replace('\n', '')))

    n_throw = int(input())

    throw_list = list(map(int, input().split()))

    for t_d, throw_h in enumerate(throw_list):
        throwing(grave_map, (-1) ** t_d, throw_h)
        find_cluster(grave_map)

    [print(''.join(row)) for row in grave_map]

if __name__ == "__main__":
    solution()
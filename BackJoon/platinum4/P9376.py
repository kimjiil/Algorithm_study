# 탈옥
import sys
from collections import defaultdict

input = sys.stdin.readline


def bfs(start, maps):
    row = len(maps)
    col = len(maps[0])
    visited_map = [[0] * col for _ in range(row)]

    q = []
    root_dic = dict()
    # for i, j in start:
    #     q.append((i, j)) #시작점
    #     visited_map[i][j] = 1

    # door_i, door_j = start
    door_q = [*start]
    door_set = set()
    while True:
        door_i, door_j = door_q.pop(0)
        q = [(door_i, door_j)]
        visited_map[door_i][door_j] = visited_map[door_i][door_j] + 1
        while q:
            i, j = q.pop(0)

            if i == 0 or j == 0 or i == row - 1 or j == col - 1:
                temp = sorted(door_set, key=lambda x: x[2])

                for idx, t in enumerate(temp):
                    if t[2] == visited_map[i][j] - 1:
                        return idx + 1

            for m in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                m_i, m_j = i + m[0], j + m[1]

                if 0 <= m_i and m_i < row and 0 <= m_j and m_j < col:
                    if maps[m_i][m_j] == '.' and visited_map[m_i][m_j] == 0:
                        q.append((m_i, m_j))
                        visited_map[m_i][m_j] = visited_map[i][j]

                    if maps[m_i][m_j] == '#':
                        if visited_map[m_i][m_j] == 0:
                            door_q.append((m_i, m_j))
                        # root_dic[(m_i, m_j)] = (door_i ,door_j)
                        # root_dic[(door_i, door_j)] = (m_i, m_j)
                            visited_map[m_i][m_j] = visited_map[i][j]
                            door_set.add((m_i, m_j, visited_map[i][j]))
                        # root_dic[(door_i, door_j)] = (m_i, m_j)

        # print()

    # print()

def solution():
    n_tc = int(input())

    for tc_i in range(n_tc):
        h, w = map(int, input().replace('\n', '').split())

        maps = []
        prisoners = []
        exits = []
        for i in range(h):
            maps.append(list(input().replace('\n', '')))

            for j in range(w):
                if maps[i][j] == '$':
                    prisoners.append((i, j))
                    maps[i][j] = '.'

                if (i == 0 or i == h-1 or j == 0 or j == w - 1) and maps[i][j] != '*':
                    # 변두리면서 벽이 아닌 경우
                    exits.append((i, j))


        print(bfs(prisoners, maps))

if __name__ == "__main__":
    answer = solution()
    print(answer)
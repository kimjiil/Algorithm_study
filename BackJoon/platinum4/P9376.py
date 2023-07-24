# 탈옥
import sys

input = sys.stdin.readline
def failure():
    def bfs(start, maps):
        row = len(maps)
        col = len(maps[0])
        visited_map = [[0] * col for _ in range(row)]

        # root_dic = dict()
        # root_dic[start] = (-1, -1)
        root_list = [[[] for _ in range(col)] for _ in range(row)]
        root_list[start[0]][start[1]].append((-1, -1))

        visited_map[start[0]][start[1]] = 1
        exit_list = []
        door_q = [start]
        while door_q:
            door_i, door_j = door_q.pop(0)
            q = [(door_i, door_j)]

            while q:

                i, j = q.pop(0)

                for m in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    m_i, m_j = i + m[0], j + m[1]

                    if 0 <= m_i and m_i < row and 0 <= m_j and m_j < col:
                        if maps[m_i][m_j] == '.' and visited_map[m_i][m_j] == 0:
                            q.append((m_i, m_j))
                            visited_map[m_i][m_j] = visited_map[i][j]

                        if maps[m_i][m_j] == '#':
                            if visited_map[m_i][m_j] == 0:
                                door_q.append((m_i, m_j))
                                visited_map[m_i][m_j] = visited_map[i][j] + 1
                                # root_dic[(m_i, m_j)] = (door_i, door_j)
                                root_list[m_i][m_j].append((door_i, door_j))

                        if (m_i == 0 or m_i == row - 1 or m_j == 0 or m_j == col - 1) and visited_map[m_i][m_j] > 0 and maps[m_i][m_j] != '#':
                            # root_dic[(m_i, m_j)] = (door_i, door_j)
                            root_list[m_i][m_j].append((door_i, door_j))

        for j in [0, col - 1]:
            for i in range(row):
                if visited_map[i][j] > 0:
                    exit_list.append((i, j))

        for i in [0, row - 1]:
            for j in range(col):
                if visited_map[i][j] > 0:
                    exit_list.append((i, j))
        return exit_list, root_list#root_dic

    def get_doors(point, root_dict, maps):
        cur = point
        doors = []
        # while cur != (-1, -1):
        #     i, j = cur
        #     if maps[i][j] == '#':
        #         doors.append((i, j))
        #     cur = root_dict[cur]

        while cur != (-1, -1):
            i, j = cur
            if maps[i][j] == '#':
                doors.append((i, j))
            cur = root_dict[i][j][0]

        return doors

    def find_min(exit_lists, root_dicts, maps):

        p1, p2 = list(exit_lists.keys())

        min_door = 10001
        for p1_exit in exit_lists[p1]:
            p1_doors = get_doors(p1_exit, root_dicts[p1], maps)
            for p2_exit in exit_lists[p2]:
                doors = set()
                p2_doors = get_doors(p2_exit, root_dicts[p2], maps)
                doors.update(p1_doors, p2_doors)

                if min_door > len(doors):
                    min_door = len(doors)

        return min_door

    import os

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
            exit_lists = dict()
            root_dicts = dict()
            for prisoner in prisoners:
                e, r = bfs(prisoner, maps)
                exit_lists[prisoner] = e
                root_dicts[prisoner] = r

            print(find_min(exit_lists, root_dicts, maps))


from collections import deque

def bfs(start, maps):

    row = len(maps)
    col = len(maps[0])

    visited_map = [[0] * col for _ in range(row)]
    s_i, s_j = start
    visited_map[s_i][s_j] = 1
    q = deque([start])
    while q:
        i, j = q.popleft()

        for m in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            m_i = i + m[0]
            m_j = j + m[1]

            if 0 <= m_i and m_i < row and  0 <= m_j and m_j < col:
                if visited_map[m_i][m_j] == 0 and maps[m_i][m_j] != '*':
                    if maps[m_i][m_j] == '.' or maps[m_i][m_j] == '$':
                        q.appendleft((m_i, m_j))
                        visited_map[m_i][m_j] = visited_map[i][j]
                    elif maps[m_i][m_j] == '#':
                        q.append((m_i, m_j))
                        visited_map[m_i][m_j] = visited_map[i][j] + 1

    return visited_map

def solution():
    n_tc = int(input())
    for n in range(n_tc):
        row, col = map(int, input().split())
        maps = [['.'] * (col + 2) for _ in range(row + 2)]

        start_point = [(0, 0)]
        for i in range(row):
            temp = list(input().replace('\n', ''))
            for j in range(col):
                maps[i + 1][j + 1] = temp[j]
                if maps[i + 1][j + 1] == '$':
                    start_point.append((i + 1, j + 1))

        visited_list = []
        for s in start_point:
            visited_list.append(bfs(s, maps))

        min_value = 214780000
        value_map = [[0] * (col + 2) for _ in range(row + 2)]
        for i in range(row + 2):
            for j in range(col + 2):
                value = 0
                if maps[i][j] == '#':
                    for k in range(3):
                        value += visited_list[k][i][j]
                    value -= 5
                    value_map[i][j] = value
                    if value < min_value and value >= 0:
                        min_value = value
                elif maps[i][j] != '*':
                    for k in range(3):
                        value += visited_list[k][i][j]
                    value -= 3
                    value_map[i][j] = value
                    if value < min_value and value >= 0:
                        min_value = value

        print(min_value)

if __name__ == "__main__":
    answer = solution()
    # print(answer)
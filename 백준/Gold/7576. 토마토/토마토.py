import sys
from collections import deque

input = sys.stdin.readline
m, n = map(int, input().split())

maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))

def solution(m, n, maps):
    direct = dict(r=(1, 0), l=(-1, 0), u=(0, -1), d=(0, 1))

    q = deque()
    for y in range(n):
        for x in range(m):
            if maps[y][x] == 1:
                q.append((x, y))

    while len(q) > 0:
        cur_x, cur_y = q.popleft()

        for key in direct:
            m_x = cur_x + direct[key][0]
            m_y = cur_y + direct[key][1]
            if m_x >= 0 and m_x < m and m_y >= 0 and m_y < n:
                if maps[m_y][m_x] == 0:
                    maps[m_y][m_x] = maps[cur_y][cur_x] + 1
                    q.append((m_x, m_y))

    max_value = 0
    for y in range(n):
        for x in range(m):
            if maps[y][x] == 0:
                return -1

            if maps[y][x] > max_value:
                max_value = maps[y][x]

    return max_value - 1
answer = solution(m, n, maps)
print(answer)
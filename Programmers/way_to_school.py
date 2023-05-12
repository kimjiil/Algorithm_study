import math
import itertools
from collections import defaultdict
def point_def(point_list):
    current_x, current_y = 0, 0
    for x, y in point_list:
        if current_x <= x and current_y <= y:
            current_x, current_y = x, y
        else:
            return False
    return True


def factorial(dict, n):
    if n in dict:
        return dict[n]
    else:
        dict[n] = math.factorial(n)
        return dict[n]


def solution(m, n, puddles):
    factorial_dict = defaultdict()
    # 모든 경로의 수
    all_root = int(factorial(factorial_dict, m + n - 2) / (factorial(factorial_dict, m - 1) * factorial(factorial_dict, n - 1)))
    not_root = 0
    root_dict = defaultdict()

    for i in range(1, len(puddles) + 1):
        per = list(itertools.combinations(puddles, i))
        for p in per:
            p = sorted(p, key=lambda x: (x[0], x[1]))
            p.append([m, n])
            if point_def(p): # 지점을 모두 통과 가능할때
                _root = 1
                start_x, start_y = 1, 1
                for coord_x, coord_y in p:
                    x = coord_x - start_x
                    y = coord_y - start_y
                    key = f's{start_x}{start_y}d{coord_x}{coord_y}'
                    if key in root_dict:
                        _root = _root * root_dict[key]
                    else:
                        root_dict[key] = int(factorial(factorial_dict, x + y) / (factorial(factorial_dict, x) * factorial(factorial_dict, y)))
                        _root = _root * root_dict[key]

                    start_x = coord_x
                    start_y = coord_y

                not_root = not_root + ((-1) ** (i+1)) * _root

    return 1000000007 % (all_root - not_root)

m = 4 ; n = 3 ; puddles = [[2, 2], [4, 2]]
result = 4

print(result == solution(m, n, puddles))


m = 4 ; n = 3 ; puddles = [[2, 2]]
result = 4

def solution(m, n, puddles):
    answer = 0
    map = [[0 for i in range(m)] for j in range(n)]
    map[0][0] = 1

    for x in range(m):
        for y in range(n):
            if not [x + 1, y + 1] in puddles:
                if x + 1 < m:
                    map[y][x + 1] += map[y][x] % 1000000007
                if y + 1 < n:
                    map[y + 1][x] += map[y][x] % 1000000007
    return map[n-1][m-1]

solution(m, n, puddles)
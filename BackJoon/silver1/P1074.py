# Z

import sys
from collections import defaultdict

input = sys.stdin.readline

maps = defaultdict()
maps[(0, 0)] = 0
maps[(1, 0)] = 1
maps[(0, 1)] = 2
maps[(1, 1)] = 3
# N, r, c = map(int, input().split())
# r행 c열 6, 6
# N = 3 일때 0 1 2 3 / 4 5 6 7
N = 2; r = 2; c = 2;
total = 0

while r > 0 or c > 0:
    if r < 2 ** (N - 1):
        y = 0
    else:
        y = 1

    if c < 2 ** (N - 1):
        x = 0
    else:
        x = 1


    total += ((2 ** (N - 1)) ** 2) * maps[(x, y)]

    r = r % (2 ** (N - 1))
    c = c % (2 ** (N - 1))

    N = N - 1

print(total)
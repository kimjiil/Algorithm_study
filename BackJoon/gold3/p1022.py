# 소용돌이 예쁘게 출력하기

import sys

input = sys.stdin.readline

y1, x1, y2, x2 = map(int, input().split())

def find_num(x1, y1):
    n = max(abs(x1), abs(y1))
    if n == 0:
        return str(1)
    a = [n, n]
    num = (2 * n + 1) ** 2
    dist = abs(n - x1) + abs(n - y1)
    # y => x
    if y1 - x1 < 0:
        return str((2 * n - 1) ** 2 + dist)
    else:
        return str((2 * n + 1) ** 2 - dist)

max_value = 1
for y in [y1, y2]:
    for x in [x1, x2]:
        value = int(find_num(x, y))
        if value > max_value:
            max_value = value

str_len = len(str(max_value))
print_list = []
for y in range(y1, y2 + 1):
    temp = []
    for x in range(x1, x2 + 1):
        temp.append(find_num(x, y).rjust(str_len) + ' ')
    print_list.append(''.join(temp))

print('\n'.join(print_list))

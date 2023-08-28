import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
seq = map(int, input().split())
a_list = [0]

for a in seq:
    if a_list[-1] < a:
        a_list.append(a)
    else:
        a_list[bisect_left(a_list, a)] = a

print(len(a_list) - 1)
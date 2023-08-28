import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())

seq = list(map(int, input().split()))
a_list = []
dp_list = []
for a in seq:
    if not a_list or a_list[-1] < a:
        a_list.append(a)
        dp_list.append(len(a_list) - 1)
    else:
        idx = bisect_left(a_list, a)
        a_list[idx] = a
        dp_list.append(idx)

answer = len(a_list)
print(answer)

str_list = []
for i in range(len(dp_list) - 1, -1, -1):
    if dp_list[i] == answer - 1:
        str_list.append(seq[i])
        answer -= 1

print(' '.join(map(str, str_list[::-1])))
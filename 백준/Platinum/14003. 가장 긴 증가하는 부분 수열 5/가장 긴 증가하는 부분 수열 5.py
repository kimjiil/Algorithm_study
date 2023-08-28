import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))
########################
# seq = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
# seq = [2, 8, 9, 5, 6, 7, 1]
# seq = [3, 5, 7, 9, 2, 1, 4, 8, 9]
# seq = [3, 5, 6, 9, 2, 1, 4, 7, 8, 9]
####################################
a_list = []

tree_idx = []
for i, a in enumerate(seq):
    if not a_list or a_list[-1] < a:
        a_list.append(a)
        tree_idx.append(len(a_list) - 1)
    else:
        idx = bisect_left(a_list, a)
        a_list[idx] = a
        tree_idx.append(idx)

answer = len(a_list)
print(answer)
result = []
for i in range(len(tree_idx) - 1, -1, -1):
    if tree_idx[i] == answer - 1:
        result.append(seq[i])
        answer -= 1
        
print(' '.join(list(map(str, result[::-1]))))
import random


def determinant(q):
    # q의 크기는 항상 3
    max_value = max(q)

    if q[1] == max_value:
        return sorted(q)[:-1]
    else:
        return q

def solution1(a):
    a = a[:]
    n = len(a)

    select_set = set()

    left_q = []
    left_min = 1000000001
    right_q = a
    mid = right_q.pop(0)
    right_min = min(right_q)
    for i in range(n):
        q = []

        if len(left_q) > 0:
            if left_in < left_min:
                left_min = left_in
            q.append(left_min)

        q.append(mid)

        left_q.append(mid)
        left_in = mid

        if len(right_q) > 0:
            if mid == right_min:
                right_min = min(right_q)
            q.append(right_min)
            mid = right_q.pop(0)

        if len(q) > 2:
            select_set = select_set.union(set(determinant(q)))
        else:
            select_set = select_set.union(set(q))

    print(select_set)
    return len(select_set)

def solution(a):
    n = len(a)

    left_value = a[0]
    right_value = a[-1]

    answer = -1

    for i in range(n):
        if left_value >= a[i]:
            left_value = a[i]
            answer += 1

        if right_value >= a[-i - 1]:
            right_value = a[-i - 1]
            answer += 1

        if left_value == right_value:
            break

    return answer
a = [9,-1,-5]
result = 3
print(solution(a))
print(solution1(a))

a = [-16,27,65,-2,58,-92,-71,-68,-61,-33]
result = 6
print(solution(a))
print(solution1(a))

a = [-16,27,65,-2,58,-92,-68,-71,-61,-33]
result = 6
print(solution(a))
print(solution1(a))

import numpy as np

for j in range(10):
    a = np.random.permutation([i for i in range(10)])
    a = list(a)
    print(a)
    result = 6
    print(solution(a))
    print(solution1(a))
    print('=' * 100)


a = [0, 8, 7, 4, 3, 6, 1, 9, 5, 2]
print(a)
print(solution(a))
print(solution1(a))
print('=' * 100)

a = [8, 0, 4, 7, 1, 2, 3, 6, 5, 9]
print(a)
print(solution(a))
print(solution1(a))
print('=' * 100)
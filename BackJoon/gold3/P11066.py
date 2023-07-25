# 파일 합치기

import sys

input = sys.stdin.readline


def recur(a):
    if len(a) == 2:
        return [sum(a)], sum(a)
    if len(a) <= 1:
        return a, 0 # 합친 원소, 든 비용

    # case1
    l1, c1 = recur(a[:2])
    l2, c2 = recur(a[2:])

    total_cost = c1 + c2 + sum(l1, l2)
    result_list = l1 + l2

    # case2
    l1, c1 = recur(a[1:3])
    l2, c2 = recur(a[3:])

    total_cost = a[0] + c1 + c2 + sum(l1, l2)

    b = recur(a[:2]) + recur(a[2:])
    c = [a[0]] + recur(a[1:3]) + recur(a[3:])
    if sum

    print()

def solution():
    T = int(input())

    for t in range(T):
        file_n = int(input())
        files = list(map(int, input().replace("\n", '').split()))

        print(recur(files))

solution()
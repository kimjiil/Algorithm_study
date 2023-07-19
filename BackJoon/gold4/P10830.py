# 행렬 제곱

'''

크기가 N X N인 행렬 A가 주어진다 이떄 A의 B제곱을 구하는 프로그램을 작성하시오

A^B의 각원소를 1000으로 나눈 나머지를 출력한다.
'''

import sys
input = sys.stdin.readline

def transpose(a):
    n = len(a)
    temp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[j][i] = a[i][j]

    return temp

def matrix_product(a, b):
    n = len(a)
    new_matrix = []
    b = transpose(b)
    for i in range(n):
        temp = []
        for j in range(n):
            s = 0
            for a_i, b_i in zip(a[i], b[j]):
                s += (a_i * b_i)
            temp.append(s % 1000)
        new_matrix.append(temp)

    return new_matrix

def recur_matrix(a, b):
    if b == 1:
        return a

    if b % 2 == 0:
        re_a = recur_matrix(a, b // 2)
        return matrix_product(re_a, re_a)
    else:
        re_a = recur_matrix(a, b // 2)
        return matrix_product(matrix_product(re_a, re_a), a)

def solution():
    n, b = map(int, input().split())
    matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j, p in enumerate(list(map(int, input().split()))):
            matrix[i][j] = p % 1000

    result = recur_matrix(matrix, b)
    [print(' '.join(list(map(str, r)))) for r in result]

if __name__ == "__main__":
    solution()
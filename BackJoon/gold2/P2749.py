# 피보나치 수 3
'''
0 1 1 2 3 5

'''
import sys

input = sys.stdin.readline

def mat_product(m1, m2):
    a, b, c = *m1[0], m1[1][1]
    d, e, f = *m2[0], m2[1][1]

    return [[(a*d + b*e) % 1000000, (a*e + b*f) % 1000000],
            [(b*d + c*e) % 1000000, (b*e + c*f) % 1000000]]
    # # temp = [[0, 0], [0, 0]]
    # #
    # # for i in range(2):
    # #     for j in range(2):
    # #         for a_i, b_i in zip(a[i], b[j]):
    # #             temp[i][j] += a_i * b_i
    # #
    # #         temp[i][j] = temp[i][j] % 1000000
    #
    # return temp

def recur_mat(n):
    p_mat = [[1, 1], [1, 0]]

    if n == 1:
        return p_mat

    if n % 2 == 0:
        re_m = recur_mat(n // 2)
        return mat_product(re_m, re_m)
    else:
        re_m = recur_mat(n // 2)
        return mat_product(mat_product(re_m, re_m), p_mat)


def solution():
    n = int(input())
    mat = recur_mat(n+ 1)

    return mat[-1][-1]



if __name__ == "__main__":
    answer = solution()
    print(answer)
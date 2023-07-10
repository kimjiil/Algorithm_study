# 프렉탈 평면

import sys

input = sys.stdin.readline

s, n, k, r1, r2, c1, c2 = map(int, input().split())

'''
시간 s일때 r1행 c1열 부터 r2, c2열까지 모습을 출력하는 프로그램
한칸을 n x n칸으로 나눔
'''

def draw_fractal(N, K, s, n, k):
    if s == 1:
        temp = []
        for i in range(N):
            start = (N - K) // 2
            if i >= start and i < start + K:
                temp.append(['0' * start + '1' * K + '0' * start])
            else:
                temp.append(['0' * N])

        return temp

    fractal = draw_fractal(N // n, K // n, s - 1, n, k)

    temp = []
    i = 0
    for i in range(n):
        for f in fractal:
            start = (n - k) // 2
            if i >= start and i < start + k:
                temp.append(''.join(''.join(f * start) + '1' * K + ''.join(f * start)))
            else:
                temp.append(''.join(f * n))

    return temp

N = n ** s
K = k * (n ** (s - 1))
a = draw_fractal(N, K, s, n, k)

temp = a[r1:r2+1]
temp2 = []
for t in temp:
    temp2.append(t[c1:c2+1])

print('\n'.join(temp2))
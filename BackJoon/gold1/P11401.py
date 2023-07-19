# 이항 계수 3

'''
자연수 N과 정수 K가 주어졌을때 이항 계수 (N K)를 1,000,000,007로 나눈 나머지를 구하라.

1 <= N <= 4,000,000
0 <= K <= N

4000000! / (2000000! * 2000000!)
'''

import sys
input = sys.stdin.readline
def power(a,b, m):
    result = 1
    while b > 0:
        if b % 2 != 0:
            result = (result *a) % m

        b = b // 2
        a = (a * a) % m
    return result

def modinverse(a, m):

    return power(a, m - 2, m)

def solution():
    r = 1000000007
    n, k = map(int, input().split())
    out = 1
    a = 1
    b = 1
    if n - k < k:
        k = n - k

    for i in range(k):
        a = (a * (n - i)) % r
        b = (b * (i + 1)) % r
        # b = modinverse((i + 1), r)
        # out = (a * b) % r
    out = (a * modinverse(b, r) % r)
    return out

if __name__ == '__main__':
    answer = solution()
    print(answer)
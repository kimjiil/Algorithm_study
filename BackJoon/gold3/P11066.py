# 파일 합치기

import sys

input = sys.stdin.readline

# 집합의 최소 비용을 계산함
def recur(files):

    if len(files) == 2:
        return sum(files)

    if len(files) == 1:
        return 0

    t = []
    for k in range(1, len(files)):
        # len 5 0 1 2 3 4
        left = recur(files[:k]) + sum(files[:k])
        right = recur(files[k:]) + sum(files[k:])
        t.append(left + right)

    return min(t)

def dp(files):

    #dp[i][j] i부터 j번쨰 파일의 부분집합의 최소 비용
    dp = [[214700000 if i != j else 0 for j in range(len(files))] for i in range(len(files))]
    sum_list = []
    s = 0
    sum_list.append(s)
    for i in files:
        s += i
        sum_list.append(s)

    for i in range(0, len(files)): # 간격
        for j in range(0, len(files) - i):
            for k in range(j, j + i):
                if i == 1:
                    dp[j][j + i] = sum_list[j + i + 1] - sum_list[j]
                else:
                    dp[j][j + i] = min(dp[j][j + i], dp[j][k] + dp[k+1][j+i] + sum_list[j + i + 1] - sum_list[j])#sum(files[j:j + i + 1]))

    return dp[0][-1]

def solution():
    T = int(input())

    for t in range(T):
        file_n = int(input())
        files = list(map(int, input().replace("\n", '').split()))

        # print(recur(files))
        print(dp(files))

solution()
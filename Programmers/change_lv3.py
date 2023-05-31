def solution(n, money):
    dp = [1] + [0] * n

    for i in range(1, n + 1):
        for m in money:
            if i - m >= 0:
                dp[i] = dp[i] + dp[i - m]

    return dp[n]

def solution(n, money):
    # dp = [[0 for i in range(n + 1)] for j in range(len(money))]
    dp = [[1 if i == 0 and j % money[0] == 0 else 0 for j in range(n + 1)] for i in range(len(money))]
    for m in range(1, len(money)):
        for i in range(n + 1):
            if i - money[m] >= 0:
                dp[m][i] = dp[m - 1][i] + dp[m][i - money[m]]
            else:
                dp[m][i] = dp[m - 1][i]
    return dp[-1][-1]


n = 5
money = [1,2,5]
result = 4
answer = solution(n, money)
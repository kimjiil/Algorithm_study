#도둑질
def solution(money):
    # 첫째집을 턴경우
    dp1 = [0] * (len(money) - 1)
    # 두번째 집부터 턴 경우
    dp2 = [0] * (len(money) - 1)
    for i in range(len(money) - 1):
        dp1[i] = max(dp1[i - 2] + money[i], dp1[i - 1])
        dp2[i] = max(dp2[i - 2] + money[i + 1], dp2[i - 1])
    return max(dp1[-1], dp2[-1])


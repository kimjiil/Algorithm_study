# 스티커 모으기
import heapq

def solution(sticker):

    if len(sticker) == 1:
        return sticker[0]

    if len(sticker) == 2:
        return max(sticker)

    dp1 = [0] * (len(sticker) - 1)
    dp2 = [0] * (len(sticker) - 1)
    for i in range(len(sticker) - 1):
        dp1[i] = max(sticker[i] + dp1[i - 2], dp1[i - 1])
        dp2[i] = max(sticker[i + 1] + dp2[i - 2], dp2[i - 1])

    return max(dp1[-1], dp2[-1])

# case 1
sticker = [14, 6, 5, 11, 3, 9, 2, 10]
result = 36
answer = solution(sticker)
if result != answer:
    print(solution(sticker), result)

# case 2
sticker = [1, 3, 2, 5, 4]
result = 8
answer = solution(sticker)
if result != answer:
    print(solution(sticker), result)
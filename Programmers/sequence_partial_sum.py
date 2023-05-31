# level 3 연속 펄스 부분 수열의 합
def solution1(sequence):
    answer = 0
    max_value = -2147000000
    status_q = []
    for s in sequence:
        if s > 0:
            status = 1
        elif s < 0:
            status = -1
        else:
            if len(status_q) > 0:
                if status == 1:
                    status = -1
                else:
                    status = 1
            else:
                continue

        if len(status_q) == 0:
            status_q.append(status)
            answer += status * s
        else:
            if status_q[-1] != status:
                status_q.append(status)
                answer += status * s
            else:
                status_q = []
                status_q.append(status)
                if max_value < answer:
                    max_value = answer
                answer = 0
                answer += status * s
    return max(answer, max_value)


def solution(sequence):
    dp = []
    for i, s in enumerate(sequence):
        if i == 0:
            dp.append(((-1) ** i) * s)
        else:
            dp.append(dp[-1] + ((-1) ** i) * s)

    dp_max = abs(max(dp) - min(min(dp), 0))
    dp_min = abs(min(dp) - max(max(dp), 0))
    return max(dp_max,dp_min)

sequence = [2, 3, -6, 1, 3, -1, 2, 4]
result = 10

answer = solution(sequence)
print(answer)
print("=" * 50)
#
#
# sequence = [2, -1, 3, 3, -3, 3]
# result = 10
#
# answer = solution(sequence)
# print(answer)
# print("=" * 50)

sequence = [2222, 1]
result = 4441

answer = solution(sequence)
print(answer)
print("=" * 50)
#
# import numpy as np
# for j in range(10):
#     sequence = list([np.random.randint(-10, 10) for i in range(10)])
#     print(sequence)
#     result = 10
#
#     answer = solution(sequence)
#     print(answer)
#     print("=" * 50)
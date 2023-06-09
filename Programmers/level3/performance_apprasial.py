# 인사 고과
import heapq

def solution(scores):
    answer = 0
    wonho = scores[0]

    max_value = 0
    sorted_list = sorted(scores[1:], key=lambda x:(-x[0], x[1]))
    for s in sorted_list:
        if s[0] > wonho[0] and s[1] > wonho[1]:
            return -1

        if sum(s) > sum(wonho):
            if max_value <= s[1]:
                max_value = s[1]
                answer += 1

    return answer


# scores = [[2,2],[1,4],[3,2],[3,2],[2,1]]
# result = 4
# answer = solution(scores)
# if result != answer:
#     print(answer)
#
# scores = [[7,7],[10,7],[9,6],[9,6]]
# result = 2
# answer = solution(scores)
# if result != answer:
#     print(answer)
#
# scores = [[7,7],[9,6],[9,6],[10,7]]
# result = 2
# answer = solution(scores)
# if result != answer:
#     print(answer)
#
#
# scores = [[7,6],[9,6],[9,6],[10,7]]
# result = -1
# answer = solution(scores)
# if result != answer:
#     print(answer)
#
#
# scores = [[10,7],[7,7],[9,6],[9,6]]
# result = 1
# answer = solution(scores)
# if result != answer:
#     print(answer)


import random

random.seed(10)
for i in range(10):
    scores = [[random.randint(1, 10), random.randint(1, 10)] for _ in range(10)]
    print(scores)
    print(sorted(scores,key=lambda x:(-x[0], x[1])))
    answer = solution(scores)
    print(answer)
    print('=' * 30)
#

# scores = [[1000, 10], [999, 9], [1001, 10], [1002, 10], [1003, 10], [1004, 10]]
# solution(scores)
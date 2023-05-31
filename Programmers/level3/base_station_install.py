# 기지국 설치
'''
제한사항
N: 200,000,000 이하의 자연수
stations의 크기: 10,000 이하의 자연수
stations는 오름차순으로 정렬되어 있고, 배열에 담긴 수는 N보다 같거나 작은 자연수입니다.
W: 10,000 이하의 자연수

'''
import math
def solution(n, stations, w):
    rails = []
    stations.append(n + w + 1)
    start = 0

    for s in stations:
        t = s - 1 - start - w
        if t > 0:
            rails.append(s - 1 - start - w)
        start = s - 1 + w + 1

    answer = 0
    _range = 2 * w + 1
    for r in rails:
        answer += math.ceil(r / _range)

    return answer


n = 11
stations = [4, 11]
w = 1
result = 3
answer = solution(n, stations, w)
print(answer == result, answer, result)


n = 16
stations = [9]
w = 2
result = 3
answer = solution(n, stations, w)
print(answer == result, answer, result)
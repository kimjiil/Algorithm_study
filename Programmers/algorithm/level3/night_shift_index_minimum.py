#야근 지수 최소화

import heapq
def solution(n, works):

    if n >= sum(works):
        return 0

    if len(works) == 1:
        return (works[0] - n) ** 2

    heap = []

    for w in works:
        heapq.heappush(heap, -w)

    for i in range(n):
        t1 = heapq.heappop(heap)
        heapq.heappush(heap, t1 + 1)

    return sum([i ** 2 for i in heap])

works = [4, 3, 3]
n = 4
result = solution(n, works)
print(result)

works = [2, 1, 2]
n = 1
result = solution(n, works)
print(result)

works = [1, 1]
n = 3
result = solution(n, works)
print(result)

works = [2, 6, 9, 100, 4, 6]
n = 40
true_result = 3773
result = solution(n, works)
print(result)


works = [4, 3, 3]
n = 5
result = solution(n, works)
print(result)
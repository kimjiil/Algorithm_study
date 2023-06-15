import heapq

def solution2(stones, k):
    heap = []
    for i in range(len(stones) - k + 1):
        heapq.heappush(heap, max(stones[i:i+k]))
    return heapq.heappop(heap)

def solution3(stones, k):
    deque = []
    min_value = 200000001
    if len(stones) == 1:
        return stones[0]

    for i, stone in enumerate(stones):
        if  i == 199999:
            print()
        if len(deque) > 0 and deque[0] < i - k + 1:
            b = deque.pop(0)

        while len(deque) > 0 and stones[deque[-1]] < stone:
            a = deque.pop(-1)

        deque.append(i)

        if i >= k - 1:
            if min_value > stones[deque[0]]:
                min_value = stones[deque[0]]

    return min_value

# 이분법
def solution(stones, k):

    right = 200000000
    left = 1

    while left <= right:
        mid = int((left + right) / 2)
        count = 0
        for stone in stones:
            if stone - mid <= 0:
                count += 1
            else:
                count = 0

            if count >= k:
                break

        if count >= k:
            right = mid - 1
        else:
            left = mid + 1

    return left

stones = [4, 10, 4, 10, 8, 10, 3, 1, 1, 2]
k = 3
result = 3
answer = solution(stones, k)
if answer != result:
    print(solution(stones, k))

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
result = 3
answer = solution(stones, k)
if answer != result:
    print(solution(stones, k))

stones = [1,1,1,1,1,1]
k = 3
result = 1
answer = solution(stones, k)
if answer != result:
    print(solution(stones, k))

stones = [1]
k = 3
result = 1
answer = solution(stones, k)
if answer != result:
    print(solution(stones, k))

stones = [i for i in range(10, 0, -1)] * 2
k = 10
solution(stones, k)

import random

for i in range(100):
    stones = [random.randint(1, 10) for i in range(10)]
    k = random.randint(1, 5)
    answer = solution(stones, k)
    result = solution2(stones, k)
    if answer != result:
        solution(stones, k)
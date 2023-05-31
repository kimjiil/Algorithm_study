# 숫자 게임
import heapq
def solution(A, B):
    # A보다 크면서 B에서 최소값
    heap_a = []
    heap_b = []

    for a, b in zip(A, B):
        heapq.heappush(heap_a, a)
        heapq.heappush(heap_b, b)

    win_list = []
    while len(heap_a) > 0 and len(heap_b) > 0:
        #각각에서 최소값을 뽑고
        a = heapq.heappop(heap_a)
        b = heapq.heappop(heap_b)

        # a보다 크면서 b에서 최소값을 찾아야됨
        while a >= b and len(heap_b) > 0:
            b = heapq.heappop(heap_b)
        if a < b:
            win_list.append([a, b])

    return len(win_list)

A = [5,1,3,7]
B = [2,2,6,8]
result = 3
answer = solution(A, B)
print(answer == result, answer, result)

A = [2,2,2,2]
B = [1,1,1,1]
result = 0
answer = solution(A, B)
print(answer == result, answer, result)

A = [2, 3, 4, 5]
B = [1, 2, 3, 4]
result = 2
answer = solution(A, B)
print(answer == result, answer, result)
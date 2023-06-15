# 단속카메라
import heapq
def solution(routes):
    heap = []
    for r in routes:
        heapq.heappush(heap, tuple(r))

    n = 0
    max_value = -30001
    min_value = -30001
    while len(heap) > 0:
        route = heapq.heappop(heap)
        _min, _max = route
        if max_value < _min:
            max_value = _max
            min_value = _min
            n += 1

        if min_value < _min:
            min_value = _min

        if max_value > _max:
            max_value = _max

    return n

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
result = 2

print(solution(routes) == result, solution(routes), result)

routes = [[-30000,15000],[15001,15002]]
result = 2

print(solution(routes) == result, solution(routes), result)

routes = [[1, 2], [2, 3], [3, 4], [4, 5], [6, 7]]
result = 3

print(solution(routes) == result, solution(routes), result)

routes = [[1, 7], [2, 7], [3, 7], [4, 7], [5, 7]]
result = 1

print(solution(routes) == result, solution(routes), result)

routes = [[1, 7], [2, 3], [3, 4], [4, 5], [5, 6]]
result = 2

print(solution(routes) == result, solution(routes), result)


print("=" * 30)
def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    last_camera = -30000

    answer = 0

    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]

    return answer

routes = [[1, 7], [2, 3], [3, 4], [4, 5], [5, 6]]
result = 2

print(solution(routes) == result, solution(routes), result)

from collections import defaultdict

def solution(n, roads, sources, destination):
    answer = []
    maps = defaultdict(list)
    for a, b in roads:
        maps[a - 1].append(b - 1)
        maps[b - 1].append(a - 1)


    dist = [-1 for i in range(n)]
    visited = [0 for i in range(n)]

    q = [destination - 1]
    visited[destination - 1] = 1
    dist[destination - 1] = 0

    while len(q) > 0:
        cur_node = q.pop(0)
        for next_node in maps[cur_node]:
            if visited[next_node] == 0:
                q.append(next_node)
                dist[next_node] = 0
                visited[next_node] = 1
                dist[next_node] = dist[cur_node] + 1

    for s in sources:
        answer.append(dist[s - 1])
    return answer


n = 3
roads = [[1, 2], [2, 3]]
sources = [2, 3]
destination = 1
result = [1, 2]
answer = solution(n, roads, sources, destination)
print(answer)

n = 5
roads = [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]]
sources = [1, 3, 5]
destination = 5
result = [2, -1, 0]
answer = solution(n, roads, sources, destination)
print(answer)

n = 5
roads = [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]]
sources = [1, 3, 5]
destination = 3
result = [-1, 0, -1]
answer = solution(n, roads, sources, destination)
print(answer)
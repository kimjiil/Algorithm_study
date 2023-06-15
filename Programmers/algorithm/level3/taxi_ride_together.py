# 합승 택시 요금
from collections import defaultdict

def get_parent(i, parent):
    if parent[i] == i:
        return i
    else:
        return get_parent(parent[i], parent)

def solution1(n, s, a, b, fares):

    parent = [i for i in range(n)]

    fares = sorted(fares, key=lambda t:t[2])

    maps = defaultdict(defaultdict)
    for i, j, fee in fares:
        if get_parent(i - 1, parent) != get_parent(j - 1, parent):
            parent[get_parent(i - 1, parent)] = get_parent(j - 1, parent)
            maps[i][j] = fee
            maps[j][i] = fee

    dist = [[] for i in range(n)]
    visited = [False] * n
    q = [s]
    visited[s - 1] = True

    while len(q) > 0:
        cur = q.pop(0)

        for next in maps[cur].keys():
            if not visited[next - 1]:
                dist[next - 1] = dist[cur - 1][:]
                dist[next - 1].append((cur, next, maps[cur][next]))
                q.append(next)
                visited[next - 1] = True

    total = []
    for dest in [a, b]:
        total += dist[dest - 1]

    answer = 0
    for t in set(total):
        answer += t[2]
    return answer

def solution(n, s, a, b, fares):
    dist = [[214700000] * n for i in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for i, j, fee in fares:
        dist[i - 1][j - 1] = fee
        dist[j - 1][i - 1] = fee


    for mid in range(n):
        for start in range(n):
            for end in range(n):
                if dist[start][end] > dist[start][mid] + dist[mid][end]:
                    dist[start][end] = dist[start][mid] + dist[mid][end]

    answer = 214700000
    for m in range(n):
        if answer > dist[s - 1][m] + dist[m][a - 1] + dist[m][b - 1]:
            answer = dist[s - 1][m] + dist[m][a - 1] + dist[m][b - 1]
    return answer
n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
result = 82
answer = solution(n, s, a, b, fares)
print(answer)

n = 7
s = 3
a = 4
b = 1
fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
result = 14
answer = solution(n, s, a, b, fares)
print(answer)

n = 6
s = 4
a = 5
b = 6
fares = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
result = 18
answer = solution(n, s, a, b, fares)
print(answer)

n = 2
s = 1
a = 2
b = 2
fares = [[1, 2, 3]]
answer = solution(n, s, a, b, fares)
print(answer)
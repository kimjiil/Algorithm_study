from collections import defaultdict

def solution(n, edge):
    answer = 0
    matrix = [[0 for i in range(n)] for i in range(n)]
    dic_idx = defaultdict(int)
    for i in range(n):
        matrix[i][i] = 1
        dic_idx[i]

    for i, j in edge:
        matrix[i - 1][j - 1] = 1
        matrix[j - 1][i - 1] = 1

    visited = [0] * n
    dist = [0] * n
    q = []

    del dic_idx[0]
    i = 0
    q.append(i)
    visited[i] = 1
    max_dist = 0

    while len(q) > 0:
        v_i = q.pop(0)
        # for j in range(n):
        #     if visited[j] == 0 and matrix[v_i][j] == 1 and v_i != j:
        #         q.append(j)
        #         visited[j] = 1
        #         dist[j] = dist[v_i] + 1
        #         if max_dist < dist[j]:
        #             max_dist = dist[j]
        key_list = list(dic_idx.keys())
        for j in key_list:
            if matrix[v_i][j] == 1:
                del dic_idx[j]
                q.append(j)
                dist[j] = dist[v_i] + 1
                if max_dist < dist[j]:
                    max_dist = dist[j]

    count = 0
    for d in dist:
        if d >= max_dist:
            count += 1

    return count

def solution(n, edge):
    adjacent = [[] for i in range(n)]
    for i, j in edge:
        adjacent[i - 1].append(j - 1)
        adjacent[j - 1].append(i - 1)

    dist = [0] * n
    visited = [0] * n
    q = []

    q.append(0)
    visited[0] = 1
    max_dist = 0

    count = 0

    while len(q) > 0:
        current_node = q.pop(0)

        for next_node in adjacent[current_node]:
            if visited[next_node] == 0:
                q.append(next_node)
                visited[next_node] = 1
                dist[next_node] = dist[current_node] + 1
                if max_dist < dist[next_node]:
                    max_dist = dist[next_node]
                    count = 0

                if max_dist <= dist[next_node]:
                    count += 1

    return count



n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
result = 3
answer = solution(n, vertex)
print(answer)
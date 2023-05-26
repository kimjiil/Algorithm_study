# 섬 연결하기

import heapq as hq
def solution2(n, costs):
    adjacent = [[] for i in range(n)]
    for i, j, cost in costs:
        # hq.heappush(adjacent[i], (cost, j))
        # hq.heappush(adjacent[j], (cost, i))
        adjacent[i].append([cost, j])
        adjacent[j].append([cost, i])

    q = []
    dist = [0] + [2140000000] * (n - 1)
    visited = [1] + [0] * (n - 1)
    q.append(0)
    selected_edge = [[0] * n for i in range(n)]
    while len(q) > 0:
        cur_node = q.pop(0)

        for cost, adj_node in adjacent[cur_node]:
            if visited[adj_node] == 0:
                q.append(adj_node)
                visited[adj_node] = 1
            if dist[adj_node] > dist[cur_node] + cost:
                dist[adj_node] = dist[cur_node] + cost
                selected_edge[adj_node][cur_node] = cost
                selected_edge[cur_node][adj_node] = cost
            # dist[adj_node] = min(dist[adj_node], dist[cur_node] + cost)

    sum = 0
    for e_l in selected_edge:
        for e in e_l:
            sum += e
    return int(sum / 2)

def find_parent(index, parent):
    if parent[index] == -1:
        return index
    else:
        return find_parent(parent[index], parent)

def set_parent(parent_index, j, parent):
    if parent[j] == -1:
        parent[j] = parent_index
    else:
        set_parent(parent_index, parent[j], parent)

import heapq
def solution(n, costs):
    min_q = []
    for i, j, cost in costs:
        if i < j:
            heapq.heappush(min_q, (cost, i, j))
        else:
            heapq.heappush(min_q, (cost, j, i))

    selected_edge = []
    parent = [-1] * n
    while len(min_q) > 0:
        cost, i, j = heapq.heappop(min_q)
        parent_i = find_parent(i, parent)
        parent_j = find_parent(j, parent)
        if parent_i != parent_j:
            selected_edge.append(cost)
            # parent[j] = find_parent(i, parent)
            set_parent(find_parent(i, parent), j, parent)

    return sum(selected_edge)
# n = 4
# costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
# result = 4
# answer = solution(n, costs)
# print(answer)

n = 6
costs = [[0, 1, 2],
         [0, 3, 1],
         [0, 2, 5],
         [1, 3, 2],
         [1, 2, 3],
         [2, 5, 5],
         [2, 4, 1],
         [2, 3, 3],
         [3, 4, 1],
         [4, 5, 2]]
result = 4
answer = solution(n, costs)
print(answer)
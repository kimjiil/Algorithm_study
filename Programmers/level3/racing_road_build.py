def move(*args):
    x, y, board, prev_dir, cost, visited, dp = args[:]
    visited.append((x, y))
    n = len(board)

    left = right = down = up = 214700000
    if x == n - 1 and y == n - 1:
        return cost

    if x + 1 < n:
        if not (x + 1, y) in visited and board[y][x + 1] == 0:
            if prev_dir == 'u' or prev_dir == 'd':
                t_cost = cost + 600
            else:
                t_cost = cost + 100
            if t_cost < dp[y][x + 1]['r']:
                dp[y][x + 1]['r'] = t_cost
                right = move(x + 1, y, board, 'r', t_cost, visited[:], dp)

    if y + 1 < n:
        if not (x, y + 1) in visited and board[y + 1][x] == 0:
            if prev_dir == 'l' or prev_dir == 'r':
                t_cost = cost + 600
            else:
                t_cost = cost + 100
            if t_cost < dp[y + 1][x]['d']:
                dp[y + 1][x]['d'] = t_cost
                down = move(x, y + 1, board, 'd', t_cost, visited[:], dp)

    if x - 1 >= 0:
        if not (x - 1, y) in visited and board[y][x - 1] == 0:
            if prev_dir == 'u' or prev_dir == 'd':
                t_cost = cost + 600
            else:
                t_cost = cost + 100
            if t_cost < dp[y][x - 1]['l']:
                dp[y][x - 1]['l'] = t_cost
                left = move(x - 1, y, board, 'l', t_cost, visited[:], dp)

    if y - 1 >= 0:
        if not (x, y - 1) in visited and board[y - 1][x] == 0:
            if prev_dir == 'l' or prev_dir == 'r':
                t_cost = cost + 600
            else:
                t_cost = cost + 100
            if t_cost < dp[y - 1][x]['u']:
                dp[y - 1][x]['u'] = t_cost
                up = move(x, y - 1, board, 'u', t_cost, visited[:], dp)

    return min(up, right, down, left)

from collections import defaultdict
def solution(board):
    x = y = 0
    dp = [[dict(r=214700000, d=214700000, u=214700000, l=214700000) for i in range(len(board))] for i in range(len(board))]
    visited = [(x, y)]
    right = move(x, y, board, 'r', 0, visited[:], dp)
    down = move(x, y, board, 'd', 0, visited[:], dp)

    return min(dp[-1][-1].values())

############################################################################################################################################

def solution(board):
    N = len(board)
    board[0][0] = 0
    visited = [[[[] for k in range(4)] for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            for t in range(4):#['r','l','d','u']: 0: r 1:d 2:l 3:u
                visited[i][j][t] = 2147000000
    q = []
    # heapq.heappush(q, (100, 0, (2, 1)))
    # heapq.heappush(q, (100, 1, (1, 2)))
    q.append((0, 0, (1, 1)))
    q.append((0, 1, (1, 1)))
    # for t in range(4): #['r','l','d','u']:
    visited[0][0][0] = 0
    visited[0][0][1] = 0

    d = []
    while len(q) > 0:
        cost, ty, (x, y) = q.pop(0)
        for_list = [[1, 0, 0, 'right'], [-1, 0, 2, 'left'], [0, 1, 1, 'down'], [0, -1, 3, 'up']]
        for a_x, a_y, dir, dir_t in for_list:
            move_x = x + a_x
            move_y = y + a_y

            if 0 < move_x <= N and 0 < move_y <= N:
                if board[move_y - 1][move_x - 1] != 1:
                    if dir % 2 != ty % 2:
                        n_cost = cost + 600
                    elif dir == ty:
                        n_cost = cost + 100
                    else: #되돌아 가는 경우
                        continue
                    if visited[move_y - 1][move_x - 1][dir] > n_cost:
                        # heapq.heappush(q, (n_cost, dir, (move_x, move_y)))
                        q.append((n_cost, dir, (move_x, move_y)))
                        visited[move_y - 1][move_x - 1][dir] = n_cost

    return min(visited[-1][-1])

# board = [[0,0,0],
#          [0,0,0],
#          [0,0,0]]
# result = 900
# answer = solution(board)
# print(answer)
#
board =[[0,0,0,0,0,0,0,1],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,1,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0,1],
        [0,0,1,0,0,0,1,0],
        [0,1,0,0,0,1,0,0],
        [1,0,0,0,0,0,0,0]]
result =3800
answer = solution(board)
print(answer)

# board =[[0,0,1,0],
#         [0,0,0,0],
#         [0,1,0,1],
#         [1,0,0,0]]
# result =2100
# answer = solution(board)
# print(answer)

# board =[[0,0,0,0,0,0],
#         [0,1,1,1,1,0],
#         [0,0,1,0,0,0],
#         [1,0,0,1,0,1],
#         [0,1,0,0,0,1],
#         [0,0,0,0,0,0]]
# result =3200
# answer = solution(board)
# print(answer)
#
# board = [
# [0, 0, 0, 0, 0],
# [0, 1, 1, 1, 0],
# [0, 0, 1, 0, 0],
# [1, 0, 0, 0, 1],
# [0, 1, 1, 0, 0]
# ]
# result = 3000
# answer = solution(board)
# print(answer)
#
board = [[0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 1, 1, 0, 1],
         [1, 0, 0, 0, 0, 1, 1, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
         [0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
         [0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
         [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 1, 0]]


answer = solution(board)
print(answer)
#

board = [[0, 0, 1],
         [0, 0, 0],
         [1, 0, 0]]

answer = solution(board)
print(answer)

board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 1, 1, 1, 1, 1, 0],
         [1, 0, 0, 1, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 0]]

answer = solution(board)
print(answer)
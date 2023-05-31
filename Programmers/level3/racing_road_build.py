
import heapq

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

board = [[0,0,0],
         [0,0,0],
         [0,0,0]]
result = 900
answer = solution(board)
print(answer)

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

board =[[0,0,1,0],
        [0,0,0,0],
        [0,1,0,1],
        [1,0,0,0]]
result =2100
answer = solution(board)
print(answer)

board =[[0,0,0,0,0,0],
        [0,1,1,1,1,0],
        [0,0,1,0,0,0],
        [1,0,0,1,0,1],
        [0,1,0,0,0,1],
        [0,0,0,0,0,0]]
result =3200
answer = solution(board)
print(answer)

board = [
[0, 0, 0, 0, 0],
[0, 1, 1, 1, 0],
[0, 0, 1, 0, 0],
[1, 0, 0, 0, 1],
[0, 1, 1, 0, 0]
]
result = 3000
answer = solution(board)
print(answer)

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


board = [[0, 0, 1],
         [0, 0, 0],
         [1, 0, 0]]

answer = solution(board)
print(answer)

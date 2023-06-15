# 미로 탈출 명령어


'''
n=m=50 이고 k=2500일 떄 maximum recursion depth exceeded while calling a python object 오류에 걸림
'''

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    dis = abs(x1 - x2) + abs(y1 - y2)
    return dis
def move(direct, point, size, dist, k, end):
    dir = dict(d=(1, 0), u=(-1, 0), l=(0, -1), r=(0, 1))
    if dist == k and point == end:
        return direct
    else:
        for m in ['d', 'l', 'r', 'u']:
            x = point[0] + dir[m][0]
            y = point[1] + dir[m][1]
            if 0 < x and x <= size[0] and 0 < y and y <= size[1]:
                if k - (dist + 1) >= distance(end, (x, y)):
                    return direct + move(m, (x, y), size, dist + 1, k, end)

    return 'impossible'

def solution_recur_depth_error(n, m, x, y, r, c, k):
    dir = dict(d=(1, 0), u=(-1, 0), l=(0, -1), r=(0, 1))
    start_point = (x, y)

    for d in ['d', 'l', 'r', 'u']:
        _x = start_point[0] + dir[d][0]
        _y = start_point[1] + dir[d][1]
        if 0 < _x and _x <= n and 0 < _y and _y <= m:
            if k - 1 >= distance((r, c), (_x, _y)): # 갈수 있는 거리 / 남은 거리
                return move(d, (_x, _y), (n, m), 1, k, (r, c))

'''
n x m 격자에서 출발점 (x, y)에서 도착점 (r, c)까지 k 번 움직여서 갈수 있는 명령어를 출력하면됨.
*제한 조건*
    1. 이동은 down left right up 4가지 방향으로 이동 할수 있고 격자 밖으로 움직일수없다.
    2. 같은 격자를 2번이상 중복 방문해도 된다.
    3. 움직인 명령어 경로를 사전순(d l r u)으로 빠른 경로으로 탈출 
    
격자탐색은 4가지 방향으로 완전 탐색을 하면 경우의 수가 너무 많아 지기 떄문에 가지치기를 해서 경우의 수를 줄여야된다.
1. 앞으로 갈 지점에서 갈수 있는 거리(k)와 남은 거리(현재점과 도착점의 최소 맨해튼 거리)를 비교해서 갈 수 있는 거리가 남은 거리
보다 작으면 이 점으로는 탐색 하지 않는다.
2. 사전순으로 탈출해야 하기때문에 d l r u 순으로 완전 탐색 하되 먼저 어느 한 방향에서 탐색 즉 1번 조건이 가능하다면
나머지 방향은 탐색 하지 않는다.

이하 방법으로 모든 프로그래머스 TC 4ms 이내 통과 가능

'''

def solution(n, m, x, y, r, c, k):
    dir = dict(d=(1, 0), u=(-1, 0), l=(0, -1), r=(0, 1))
    move_list = []
    _x = x
    _y = y
    current_dist = 1
    moving = True
    while current_dist <= k and moving:
        moving = False
        for d in ['d', 'l', 'r', 'u']:
            move_x = x + dir[d][0]
            move_y = y + dir[d][1]
            if 0 < move_x and move_x <= n and 0 < move_y and move_y <= m:
                if k - current_dist >= distance((r, c), (move_x, move_y)):  # 갈수 있는 거리 / 남은 거리
                    x = move_x
                    y = move_y
                    current_dist += 1
                    move_list.append(d)
                    moving = True
                    break

    if current_dist == k + 1 and (r, c) == (x, y):
        return ''.join(move_list)
    else:
        return 'impossible'


if __name__ == '__main__':
    import ast

    inout_example = '''
n	m	x	y	r	c	k	result
3	4	2	3	3	1	5	"dllrl"
2	2	1	1	2	2	2	"dr"
3	3	1	2	3	3	4	"impossible"
'''
    inout_example = inout_example.replace(' ', '')
    temp = [s for s in inout_example.split('\n') if s != '']
    key = temp[0].split('\t')
    for test_case in temp[1:]:
        args = list(map(ast.literal_eval, test_case.split('\t')))
        result = args[-1]
        answer = solution(*args[:-1])
        print(result, '/', answer)

n = 3; m = 3; x = 1; y = 1; r = 3; c = 3 ; k =4; result = "ddrr"
answer = solution(n, m, x, y, r, c, k)
print(result, '/', answer)

n = 50; m = 50; x = 1; y = 1; r = 50; c = 50 ; k =100; result = ""
answer = solution(n, m, x, y, r, c, k)
print(result, '/', answer)

n = 3; m = 3; x = 2; y = 2; r = 3; c = 3; k = 2; result = ""
answer = solution(n, m, x, y, r, c, k)
print(result, '/', answer)
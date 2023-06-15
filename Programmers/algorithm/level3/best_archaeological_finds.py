# 고고학 최고의 발견


'''
시계들의 행렬
각 칸마다 시계 바늘이 1개 있고 이 바늘은 시계 방향으로 90도씩 회전 가능
어떤 한 칸의 시계 바늘을 돌릴 경우 인근의 상하좌우 시계 바늘도 같이 돌아감
모든 시계 바늘이 12시를 가르키면 퍼즐이 해결됨

최소한의 조작 횟수로 퍼즐을 해결
0: 12시 / 1: 3시 / 2: 6시 / 3: 9시

clockhands는 2 ~ 8 사이의 크기 원소는 0 ~ 3

[
[0,3,3,0],
[3,2,2,3],
[0,3,2,0],
[0,3,3,3]]

circular queue로 0이 4번 돌아간지 0번 돌아간지 모름..

반시계로 돌아갔던걸 다시 시계로 돌리면 0이된다.
위의 매트릭스를 반시계 방향의 방향으로 나타내면

[-4, -1, -1, -4]
[-1, -2, -2, -1]
[-4, -1, -2, -4]
[-4, -1, -1, -1]

이때 -4는 0번 일수도 반시계로 4번 일수도 있음..

최소값을 위해 1번째로 0일떄로 가정 하고 2번쨰로 -4 일때로 가정해서 탐색

[ 0, -1, -1,  0]
[-1, -2, -2, -1]
[ 0, -1, -2,  0]
[ 0, -1, -1, -1]

---------------------

[[3, 2, 0, 3],
[2, 0, 1, 2],
[1, 1, 0, 2],
[2, 2, 1, 1]]

[[-1, -2, -4, -1],
[-2, -4, -3, -2],
[-3, -3, -4, -2],
[-2, -2, -3, -3]]

1) 반시계 방향의 성분으로 모두 변경
2) 이때 가장 큰값을 가장 많이 가지고 있는 좌표를 기준(이떄 이 좌표 근처에 0으로 변함 점이 없어야됨)
3) 이때 모든 값이 0 또는 -4 이면 해결

'''

# direction 1 => 시계 방향 -1 은 반시계
def _turn_clock(point, direction, clocks):
    x, y = point
    n = len(clocks)
    direct = dict(c=(0, 0), u=(0, -1), d=(0, 1), r=(1, 0), l=(-1, 0))

    for d in direct.keys():
        _x = x + direct[d][0]
        _y = y + direct[d][1]
        if 0 <= _x and _x < n and 0 <= _y and _y < n:
            clocks[_y][_x] = (clocks[_y][_x] + direction) % 4
            # clocks[_y][_x] = clocks[_y][_x] + direction


from collections import deque
import random
random.seed(0)

def create_problem(n, result):
    clockhands = [[0 for _ in range(n)] for _ in range(n)]

    turn_list = deque()
    for i in range(result):
        random_point = (random.randint(0, n - 1), random.randint(0, n-1))
        _turn_clock(random_point, -1, clockhands)
        turn_list.appendleft(random_point)

    return clockhands, turn_list, result

from collections import defaultdict

def is_solved(clockhands):
    n = len(clockhands)

    for y in range(n):
        for x in range(n):
            # 0 이거나 -4이면 계속 진행
            # 하나라도 0, -4가 아니면 return False
            if divmod(clockhands[y][x], 4)[1] != 0:
                return False

    return True

def block_point(point, blocks):
    x, y = point
    direct = dict(c=(0, 0), u=(0, -1), d=(0, 1), r=(1, 0), l=(-1, 0))
    n = len(blocks)

    for d in direct.keys():
        _x = x + direct[d][0]
        _y = y + direct[d][1]
        if 0 <= _x and _x < n and 0 <= _y and _y < n:
            if not blocks[_y][_x]:
                return False
    return True

def turn_clock(point, direction, clocks, blocks):
    x, y = point
    n = len(clocks)
    direct = dict(c=(0, 0), u=(0, -1), d=(0, 1), r=(1, 0), l=(-1, 0))

    for d in direct.keys():
        _x = x + direct[d][0]
        _y = y + direct[d][1]
        if 0 <= _x and _x < n and 0 <= _y and _y < n:
            clocks[_y][_x] = (clocks[_y][_x] + direction) % 4
            # clocks[_y][_x] = clocks[_y][_x] + direction
            # if clocks[_y][_x] == 0:
            #     blocks[_y][_x] = False

# 실패한 솔루션
def solution_fail(clockHands):
    answer = 0
    direct = dict(c=(0, 0), u=(0, -1), d=(0, 1), r=(1, 0), l=(-1, 0))

    n = len(clockHands)

    rim = []
    corner = []
    center = []
    for y in range(n):
        for x in range(n):
            if divmod(x, n - 1)[1] == 0 and divmod(y, n - 1)[1] == 0:  # 모서리
                corner.append((x, y))
            elif divmod(x, n - 1)[1] == 0 or divmod(y, n - 1)[1] == 0:  # 변두리
                rim.append((x, y))
            else:  # 중앙 부분
                center.append((x, y))

    point_ordered = center + rim + corner

    blocks = [[True for _ in range(n)] for _ in range(n)]

    counter = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(4)]
    for y in range(n):
        for x in range(n):
            clockHands[y][x] = clockHands[y][x] - 4
            if clockHands[y][x] == -4:
                clockHands[y][x] = 0
            for d in direct.keys():
                _x = x + direct[d][0]
                _y = y + direct[d][1]
                if 0 <= _x and _x < n and 0 <= _y and _y < n:
                    counter[clockHands[y][x]][_y][_x] += 1

    while not is_solved(clockHands): # 퍼즐이 해결됬을때 반복문 종료
        counter = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(4)]
        for y in range(n):
            for x in range(n):
                for d in direct.keys():
                    _x = x + direct[d][0]
                    _y = y + direct[d][1]
                    if 0 <= _x and _x < n and 0 <= _y and _y < n:
                        counter[clockHands[y][x]][_y][_x] += 1

        max_value = 0
        max_idx = (0, 0)
        min_value = 0
        count_idx = -1
        while max_value == 0:
            for x, y in point_ordered:
                print((x, y), counter[count_idx][y][x], counter[-4][y][x])
                if counter[count_idx][y][x] - counter[-4][y][x] >= max_value and block_point((x, y), blocks): # 최소값일 경우
                    if max_value == counter[count_idx][y][x]:
                        if min_value > clockHands[y][x]: # 값이 같은경우만 비교
                            max_value = counter[count_idx][y][x]
                            max_idx = (x, y)
                            min_value = clockHands[y][x]
                    else:
                        max_value = counter[count_idx][y][x]
                        max_idx = (x, y)
                        min_value = clockHands[y][x]

            count_idx -= 1
        turn_clock(max_idx, 1, clockHands, blocks)
        answer += 1

    return answer



# 힌트 보고품

from itertools import product

def is_solved(clockhands):
    n = len(clockhands)

    for y in range(n):
        for x in range(n):
            # 0 이거나 -4이면 계속 진행
            # 하나라도 0, -4가 아니면 return False
            if divmod(clockhands[y][x], 4)[1] != 0:
                return False

    return True
def turn_clock(point, direction, clocks):
    x, y = point
    n = len(clocks)
    direct = dict(c=(0, 0), u=(0, -1), d=(0, 1), r=(1, 0), l=(-1, 0))

    for d in direct.keys():
        _x = x + direct[d][0]
        _y = y + direct[d][1]
        if 0 <= _x and _x < n and 0 <= _y and _y < n:
            clocks[_y][_x] = (clocks[_y][_x] + direction) % 4
def solution(clockHands):

    n = len(clockHands)
    case_list = product(range(4), repeat=n)

    min_count = 64 * 4
    for case in case_list:
        turn_count = 0
        clocks = [clockHands[y][:] for y in range(n)]
        # 첫째줄의 case
        for i, c in enumerate(case):
            turn_clock((i, 0), c, clocks)
            turn_count += c

        # 첫째줄 이후는 종속됨
        for y in range(1, n):
            for x in range(n):
                if clocks[y - 1][x] != 0:
                    turn_count = turn_count + 4 - clocks[y - 1][x]
                    turn_clock((x, y), 4 - clocks[y - 1][x], clocks)


        if is_solved(clocks):
            if min_count > turn_count:
                min_count = turn_count

    return min_count


if __name__ == '__main__':
    import ast

    inout_example = '''
clockHands	result
[[0,3,3,0],[3,2,2,3],[0,3,2,0],[0,3,3,3]]	3
'''
    inout_example = inout_example.replace(' ', '')
    temp = [s for s in inout_example.split('\n') if s != '']
    key = temp[0].split('\t')
    for test_case in temp[1:]:
        args = list(map(ast.literal_eval, test_case.split('\t')))
        result = args[-1]
        answer = solution(*args[:-1])
        print(result, '/', answer)

    clockhands, turn_list, result = create_problem(4, 10)
    answer = solution(clockhands)
    print(result, '/', answer)

    for i in range(1, 10):
        clockhands, turn_list, result = create_problem(4, i)
        # print(clockhands)
        # print(turn_list)
        answer = solution(clockhands)
        print(result, '/', answer)

'''


'''
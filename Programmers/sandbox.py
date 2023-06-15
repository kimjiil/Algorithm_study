
def solution(clockHands):
    N = len(clockHands)
    dp = [[0] * N for _ in range(N)]

    def setting(p, N):
        dp = p[0]
        while True:
            yield 0
            dp[N - 1] += 1
            idx = N - 1
            while dp[idx] == 4:
                dp[idx] = 0
                idx -= 1
                dp[idx] += 1
            if idx == -1:
                break

    def get_neighbor(dp,i,j,N):
        rt = dp[i][j]
        if i>0:
            rt += dp[i-1][j]
        if i<N-1:
            rt += dp[i+1][j]
        if j>0:
            rt += dp[i][j-1]
        if j<N-1:
            rt += dp[i][j+1]
        return rt

    answer = N * N * 4 + 1

    for k in setting(dp, N):
        ct = sum(dp[0])
        for i in range(1, N):
            for j in range(N):
                clicks = get_neighbor(dp,i-1,j,N)
                clicks += clockHands[i-1][j]
                dp[i][j] += -clicks
                dp[i][j] %= 4
                ct += dp[i][j]
        valid = True
        for j in range(N):
            clicks = get_neighbor(dp,N-1,j,N)
            clicks += clockHands[N-1][j]
            if clicks%4 == 0:
                continue
            else:
                valid = False
                break
        if valid == True:
            answer = min(answer, ct)
    assert answer != N * N * 4 + 1
    return answer

from collections import deque
import random
random.seed(0)

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

def create_problem(n, result):
    clockhands = [[0 for _ in range(n)] for _ in range(n)]

    turn_list = deque()
    for i in range(result):
        random_point = (random.randint(0, n - 1), random.randint(0, n-1))
        _turn_clock(random_point, -1, clockhands)
        turn_list.appendleft(random_point)

    return clockhands, turn_list, result

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
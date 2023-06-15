def move(x, y, key):
    N = len(key)
    _key = [[0 for i in range(N)] for j in range(N)]

    for x_i in range(N):
        if x_i + x >= 0 and x_i + x < N:
            for y_i in range(N):
                if y_i + y >= 0 and y_i + y < N:
                    _key[y_i + y][x_i + x] = key[y_i][x_i]

    return _key

def rotate(angle, key):
    for i in range(int(angle / 90)):
        key = rotate_90(key)

    return key
def rotate_90(key):
    # 시계 방향으로 회전
    N = len(key)
    _key = [[0 for i in range(N)] for j in range(N)]

    for y in range(N - 1, -1, -1):
        for x in range(N):
            _key[x][N - 1 - y] = key[y][x]

    return _key

def key_lock(key, lock):
    M = len(key)
    N = len(lock)

    if M == N:
        return key, lock
    else:
        _key = [[0 for i in range(N)] for j in range(N)]
        for i in range(M):
            for j in range(M):
                _key[i][j] = key[i][j]

        return _key, lock

def lock_key_fit(key, lock):
    s = 0
    N = len(lock)
    for x in range(N):
        for y in range(N):
            s = s + int(key[y][x] ^ lock[y][x])

    return s

def solution(key, lock):
    key, lock = key_lock(key, lock)

    N = len(lock)
    a = N ** 2
    # 키의 돌기수가 lock의 홈보다 적은 경우
    key_fit = sum([sum(k) for k in key]) # 키의 홈의 갯수
    lock_fit = N ** 2 - sum([sum(k) for k in lock]) # 남은 홈의 갯수
    if lock_fit > key_fit:
        return False
    else:
        for rot in [0, 90, 180, 270]:
            for move_x in range(-N, N + 1):
                for move_y in range(-N, N + 1):
                    _key = rotate(rot, key)
                    _key = move(move_x, move_y, _key)
                    if a == lock_key_fit(_key, lock):
                        return True
    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
result = True
answer = solution(key, lock)
print(answer)
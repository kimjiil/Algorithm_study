
def build_available(x, y, t, answer):
    if t == 1: # 보
        if [x - 1, y, 1] in answer and [x + 1, y, 1] in answer:
            return True

        if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer:
            return True
    elif t == 0: # 기둥
        if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
            return True

    return False
def solution(n, build_frame):
    answer = []

    for x, y, t, d in build_frame:
        print(x, y, t, d)
        if d == 1: # 생성
            if build_available(x, y, t, answer):
                answer.append([x, y, t])
        elif d == 0: # 제거
            answer.remove([x, y, t])
            for a_x, a_y, a_t in answer:
                if not build_available(a_x, a_y, a_t, answer):
                    answer.append([x, y, t])
                    break

    answer = sorted(answer, key=lambda x: (x[0], x[1], x[2]))
    return answer


# n = 5
# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
# result = [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
# answer = solution(n, build_frame)
# print(answer)
# print(result)
# print('=' * 30)

n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
result = [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
answer = solution(n, build_frame)
print(answer)
print(result)
print('=' * 30)

n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],
               [4,0,0,0],[1,1,1,0],[2,1,1,0], [3,1,1,0]]
result = [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
answer = solution(n, build_frame)
print(answer)
print(result)
print('=' * 30)

n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],
               [2,1,1,0]]
result = [[0,0,0],[0,1,1],[1,1,1],[2,0,0],[3,1,1],[4,0,0]]
answer = solution(n, build_frame)
print(answer)
print(result)
print('=' * 30)

n = 5
build_frame = [[0,0,0,1],[0,1,0,1],[0,2,0,1]]
result = [[0,0,0],[0,1,0],[0,2,0]]
answer = solution(n, build_frame)
print(answer)
print(result)
print('=' * 30)

n = 5
build_frame = [[0,0,0,1],[0,1,0,1],[0,2,0,1], [0,1,0,0]]
result = [[0,0,0],[0,1,0],[0,2,0]]
answer = solution(n, build_frame)
print(answer)
print(result)
print('=' * 30)
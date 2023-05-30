# 순위

def solution(n, results):
    answer = 0
    win_map = [[0 for i in range(n)] for j in range(n)]

    log = dict()
    for i in range(1, n + 1):
        log[i] = [set([]), set([])] # 왼쪽 리스트는 n을 이긴 목록, 오른쪽 리스트는 n에게 진 목록

    for win, lose in results:
        log[win][1].add(lose)
        log[lose][0].add(win)
        win_map[lose - 1][win - 1] = 1

    win_q = []
    lose_q = []
    for i in range(1, n + 1):
        win_q = win_q + list(log[i][1])
        lose_q = lose_q + list(log[i][0])
        while len(win_q) > 0:
            next_q = win_q.pop(0)
            log[i][1] = log[i][1].union(log[next_q][1])
            win_q = win_q + list(log[next_q][1])

    for i in range(1, n + 1):
        log_len = len(log[i][0]) + len(log[i][1]) + 1
        if log_len == n:
            answer += 1

    return answer

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
result = 2
answer = solution(n, results)
print(answer)
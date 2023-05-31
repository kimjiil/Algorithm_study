# 순위

def solution(n, results):
    answer = 0
    map = [[0 for i in range(n)] for j in range(n)]

    for win, lose in results:
        map[lose - 1][win - 1] = 1
        map[win - 1][lose - 1] = -1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if map[i][k] == 1 and map[k][j] == 1:
                    map[i][j] = 1
                    map[j][i] = -1

    for i in range(n):
        a = sum([abs(m) for m in map[i]])
        if a == (n - 1):
            answer += 1
    return answer

def solution1(n, results):
    answer = 0

    return answer

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
result = 2
answer = solution(n, results)
print(answer)
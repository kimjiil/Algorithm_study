def solution(board, skill):
    answer = 0

    for t, r1, c1, r2, c2, degree in skill:
        for i in range(c1, c2 + 1):
            for j in range(r1, r2 + 1):
                answer += 1
    return answer

import numpy as np

def solution(board, skill):
    answer = 0
    # skill_sum = numpy.zeros_like(board)
    row_n = len(board)
    col_n = len(board[0])
    skill_sum = np.zeros((row_n + 1, col_n + 1))
    for t, r1, c1, r2, c2, degree in skill:
        if t == 1:
            degree = -degree
        skill_sum[r1][c1] += degree
        skill_sum[r1][c2 + 1] += -degree
        skill_sum[r2 + 1][c1] += -degree
        skill_sum[r2 + 1][c2 + 1] += degree

    for r in range(row_n + 1):
        for c in range(1, col_n + 1):
            skill_sum[r][c] = skill_sum[r][c-1] + skill_sum[r][c]

    for c in range(col_n + 1):
        for r in range(1, row_n + 1):
            skill_sum[r][c] = skill_sum[r - 1][c] + skill_sum[r][c]

    result = np.array(board) + skill_sum[:row_n, :col_n]
    return sum(sum(result > 0))
board = [[5,5,5,5,5],
         [5,5,5,5,5],
         [5,5,5,5,5],
         [5,5,5,5,5]]
skill = [[1,0,0,3,4,4],
         [1,2,0,2,3,2],
         [2,1,0,3,1,2],
         [1,0,1,3,3,1]]
result = 10
answer = solution(board, skill)

board = [[1,2,3],
         [4,5,6],
         [7,8,9]]
skill = [[1,1,1,2,2,4],
         [1,0,0,1,1,2],
         [2,2,0,2,0,100]]
result = 6
answer = solution(board, skill)
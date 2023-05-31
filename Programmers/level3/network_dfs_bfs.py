n = 3
computers = [[1, 1, 0],
             [1, 1, 0],
             [0, 0, 1]]
result = 2


def solution(n, computers):
    answer = 0

    visited = [0] * n
    for idx in range(n):
        queue = []
        if visited[idx] == 0: # 방문 하지 않는 노드만
            queue.append(idx)
            while len(queue) > 0:
                current_i = queue.pop(0)
                for i in range(n):
                    if computers[current_i][i] == 1 and visited[i] == 0:
                        queue.append(i)
                        visited[i] = 1
            answer += 1
    return answer

print(solution(n, computers) == result)

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
result = 1

if not solution(n, computers) == result:
    print()

print(solution(n, computers) == result)


n = 3
computers = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
result = 3

if not solution(n, computers) == result:
    print()

print(solution(n, computers) == result)

n = 4
computers = [[1, 0, 1, 0],
             [0, 1, 0, 1],
             [1, 0, 1, 0],
             [0, 1, 0, 1]]
result = 2

if not solution(n, computers) == result:
    print()

print(solution(n, computers) == result)

n= 4
computers = [[1, 1, 0, 0],
             [1, 1, 0, 0],
             [0, 0, 1, 1],
             [0, 0, 1, 1]]
result = 2

if not solution(n, computers) == result:
    print()

print(solution(n, computers) == result)

n = 4
computers = [[1, 1, 1, 1],
             [1, 1, 1, 1],
             [1, 1, 1, 1],
             [1, 1, 1, 1]]
result = 1

if not solution(n, computers) == result:
    print()

print(solution(n, computers) == result)

n = 5
computers = [[1, 0, 0, 0, 1],
             [0, 1, 0, 0, 0],
             [0, 0, 1, 0, 0],
             [0, 0, 0, 1, 0],
             [1, 0, 0, 0, 1]]

result = 4

if not solution(n, computers) == result:
    print()
print(solution(n, computers) == result)

n = 4
computers = [[1, 1, 0, 0],
             [1, 1, 1, 0],
             [0, 1, 1, 1],
             [0, 0, 1, 1]]
result = 1

if not solution(n, computers) == result:
    print()

print(solution(n, computers) == result)
import numpy as np

def create_sample(n):
    m = list(np.eye(n, dtype=np.int32))
    for i in range(n):
        for j in range(n):
            if i < j:
                m[i][j] = 1
                m[i][j] = 1
                result = n - 1
                if not solution(n, m) == result:
                    print(i,j,n,  solution(n, m))
            m = list(np.eye(n))


create_sample(100)
'''
1) insert root A
[A]
2) pop 
3) pop된 원소의 연결된 원소를 insert
[B]
4) pop
5) pop된 원소의 연결된 원소를 insert
[]
=> end
result += 1
그 다음 원소 C
'''
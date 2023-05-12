# 최고의 집합

def solution(n, s):
    answer = []
    # n일때 가능한 s의 최소값 제한
    if s < n:
        return [-1]
    else:
        best = s // n
        rest = s % n

        for i in range(n):
            if i>= n - rest:
                answer.append(best + 1)
            else:
                answer.append(best)
    return answer

func = lambda n, s: [-1] if s < n else [s // n + 1 if i >= n - s % n else s // n for i in range(n)]

print(solution(2, 9))
print(func(2,9))
print(solution(3, 9))
print(func(3,9))
print(solution(4, 9))
print(func(4,9))
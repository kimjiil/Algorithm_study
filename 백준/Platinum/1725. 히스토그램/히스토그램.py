import sys

input = sys.stdin.readline

n = int(input())
stack = []  # (idx, h)
max_value = 0
for i in range(n + 1):
    if i == n:
        h = 0
    else:
        h = int(input())

    idx = i
    while stack and stack[-1][1] > h: # 스택보다 작은 높이가 들어올 경우
        idx, last_h = stack.pop()
        w = i - idx
        area = w * last_h
        max_value = max(max_value, area)

    if not stack or stack[-1][1] < h:
        stack.append((idx, h))

print(max_value)

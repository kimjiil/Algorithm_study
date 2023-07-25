import sys

input = sys.stdin.readline

n = int(input())
stack = []  # (idx, h)
max_value = 0
for i in range(n + 1):
    if i == n:
        h = 0 # 마지막에 0을 집어 넣어서 자동으로 stack이 비워지면서 넓이 계산하도록 함
    else:
        h = int(input())

    idx = i # stack에서 가장 마지막에 나온 idx를 저장하기 위함..
    while stack and stack[-1][1] > h: # 스택보다 작은 높이가 들어올 경우
        idx, last_h = stack.pop()
        max_value = max(max_value, (i - idx) * last_h)

    if not stack or stack[-1][1] < h:
        stack.append((idx, h))

print(max_value)

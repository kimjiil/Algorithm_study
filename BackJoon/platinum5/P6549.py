# 히스토그램에서 가장 큰 직사각형
from collections import defaultdict
import sys

input = sys.stdin.readline

import heapq

from collections import deque
from bisect import bisect_left, bisect_right

def solution():
    while True:
        input_list = map(int, input().replace("\n", '').split())

        stack = [0]  # (idx, h)
        max_value = 0

        for i, h in enumerate(input_list):
            if i == 0:
                continue

            while len(stack) != 0 and input_list[stack[-1]] > h:
                check = stack[-1]
                stack.pop()
                max_value = max(max_value, input_list[check] * (i - stack[-1] - 1))

            stack.append(i)

        print(max_value)


def sol(input_list):
    # input_list = map(int, input().replace("\n", '').split())

    # n = next(input_list)
    n = input_list[0]
    input_list = input_list[1:]
    if n == 0:
        return
    stack = [(-1, -1)]  # (idx, h)
    max_value = 0

    for i, h in enumerate(input_list):
        if stack[-1][1] < h:
            stack.append((i, h))
        else:
            while stack[-1][1] >= h:
                idx, last_h = stack.pop()
                w = i - idx
                max_value = max(max_value, last_h * w)
                w_start_i = idx
            stack.append((w_start_i, h))

    while stack:
        i, h = stack.pop()
        w = n - i
        max_value = max(max_value, h * w)
    print(max_value)

    return max_value

def true_sol(graph):
    # graph = list(map(int, stdin.readline().split()))

    # 0이 입력되면 반복문을 종료합니다.
    if graph[0] == 0:
        return None

    # 스택과 최대 직사각형 넓이를 저장할 변수를 초기화합니다.
    stack = []
    max_result = 0

    for i, height in enumerate(graph):
        if i == 0:  # 첫 번째 i는 막대기의 개수를 의미하므로 넘어갑니다.
            continue

        # 스택의 가장 위쪽 막대기보다 현재 막대기의 높이가 작으면
        if stack and stack[-1][1] > height:
            while stack:  # 스택에서 빼내며 최대 직사각형 넓이를 계산합니다.
                stack_i, stack_height = stack.pop()
                width_start = 1
                if stack:
                    width_start = stack[-1][0] + 1
                result = (i - width_start) * stack_height
                max_result = max(result, max_result)  # 최대값 갱신
                # 스택에 들어있는 막대 중에서 현재 막대의 길이보다 큰 것들만 꺼내서 계산합니다.
                if not stack or stack[-1][1] <= height:
                    break

        # 스택이 비어 있거나 스택의 가장 위쪽 막대기보다 현재 막대기의 높이가 크거나 같으면
        if not stack or stack[-1][1] <= height:
            stack.append((i, height))  # 스택에 현재 막대기를 추가합니다.

    # 반복이 종료되고, 스택에 남은 막대기가 있다면 계산합니다.
    while stack:
        stack_i, stack_height = stack.pop()
        width_start = 1
        if stack:
            width_start = stack[-1][0] + 1
        result = (graph[0] + 1 - width_start) * stack_height
        max_result = max(result, max_result)  # 최대값 갱신

    # 최대 직사각형 넓이를 출력합니다.
    print(max_result)
    return max_result

def solution1():
    while True:
        input_list = map(int, input().replace("\n", '').split())
        if input_list[0] == 0:
            return ""

        n = input_list[0]
        h_list = input_list[1:]

        h_heap = [0]
        dic = defaultdict(int)
        max_value = 0
        for i, h in enumerate(h_list):
            if h == 0:
                h_heap = [0]
                dic = defaultdict(int)
            elif -h_heap[0] < h:
                heapq.heappush(h_heap, -h)
                dic[h] = 0
                for key in dic:
                    dic[key] += (key)
            elif -h_heap[0] == h:
                for key in dic:
                    dic[key] += (key)
            else:
                num = 0
                while -h_heap[0] >= h:
                    _h = -heapq.heappop(h_heap)
                    num = int(dic[_h] / _h)
                    del dic[_h]

                heapq.heappush(h_heap, -h)
                dic[h] = num * h

                for key in dic:
                    dic[key] += (key)


            for key in dic:
                if max_value < dic[key]:
                    max_value = dic[key]
        print(max_value)
if __name__ == "__main__":
    solution()
    # import random
    # n = 100000
    # while True:
    #     n = random.randint(1, 100000)
    #     g = [n] + [random.randint(0, 1000000000) for _ in range(n)]
    #     a = true_sol(g)
    #     b = sol(g)
    #     if a != b:
    #         print(g , a, b)
    #         break
# 히스토그램에서 가장 큰 직사각형
from collections import defaultdict
import sys

input = sys.stdin.readline

import heapq

from collections import deque
from bisect import bisect_left, bisect_right

def solution():
    while True:
        input_list = list(map(int, input().replace("\n", '').split()))
        if input_list[0] == 0:
            return ""
        h_list = input_list[1:]

        h_q = deque()
        cnt_q = deque()
        cnt = 0
        for h in h_list:
            if len(h_q) == 0:
                h_q.append(h)
                cnt_q.append(cnt)
                cnt += 1
            else:
                idx = bisect_left(h_q, h)
                idx_ = bisect_right(h_q, h)
                print()

def solution1():
    while True:
        input_list = list(map(int, input().replace("\n", '').split()))
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
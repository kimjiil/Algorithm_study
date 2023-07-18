# 가운데를 말해요
import random
import sys
import heapq

input = sys.stdin.readline
# random.seed(1004)
n = int(input())
left_q = [-int(input())]
##########################
# n = 7
# seq = [1, 5, 2, 10, -99, 7 ,5]
# seq = [random.randint(1, 10) for _ in range(10)]
# print(seq)
#############################

# left_q = [-seq[0]]
right_q = []
print(-left_q[0])
# for s in seq[1:]:
for _ in range(n - 1):
    num = int(input())
    # num = s
    if num > -left_q[0]:
        # heapq.heappush(right_q, num)
        # while len(left_q) < len(right_q):
        #     heapq.heappush(left_q, -heapq.heappop(right_q))
        if len(left_q) == len(right_q):
            heapq.heappush(left_q, -heapq.heappushpop(right_q, num))
        else:
            heapq.heappush(right_q, num)

    else:
        # heapq.heappush(left_q, -num)
        # while len(left_q) - len(right_q) > 1:
        #     heapq.heappush(right_q, -heapq.heappop(left_q))
        if len(left_q) - len(right_q) >= 1:
            heapq.heappush(right_q, -heapq.heappushpop(left_q, -num))
        else:
            heapq.heappush(left_q, -num)

    print(-left_q[0])
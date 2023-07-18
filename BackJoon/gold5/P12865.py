# 평범한 배낭

'''
1 <= N <= 100 갯수
1 <= K <= 100,000 무게
1 <= V <= 1,000 가치
'''

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
K += 1

bag_list = [tuple(map(int, input().split())) for _ in range(N)]

bag_list.sort(reverse=True)

dp = {0: 0}

# for w, v in bag_list: # w: weight , v: value
#     temp = {}
#     for dp_w, dp_v in dp.items():
#         new_w = dp_w + w
#         if K >= new_w:
#             temp[new_w] = max(dp[dp_w] + v, dp.get(new_w, 0))
#     dp.update(temp)

for w, v in bag_list:
    temp = {}
    for dp_v, dp_w in dp.items():
        if dp.get(new_v := dp_v + v, K) > (new_w := dp_w + w):
            temp[new_v] = new_w
    dp.update(temp)

# print(max(dp.values()))
print(max(dp.keys()))

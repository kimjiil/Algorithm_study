def solution(triangle):
    answer = 0
    H = len(triangle)  # 5
    dp = [triangle[0]]
    for h, tri in enumerate(triangle[1:]):
        dp_list = [[] for _ in range(len(tri))]
        for idx, d in enumerate(dp[h]):  # tri : 8, 1, 0 // dp : 10 , 15
            for i in range(2):
                temp = d + tri[idx + i]
                dp_list[idx + i].append(temp)

        temp2 = []
        for d in dp_list:
            temp2.append(max(d))
        dp.append(temp2)

    return max(dp[-1])


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
result = 30

solution(triangle)
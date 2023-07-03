# 물병
# 이진법으로 변환했을떄 1의 개수가 k보다 작을 경우


import sys
input = sys.stdin.readline

# n, k = map(int, input().split())

n = 888
k = 2
min_rest = 10 ** 7

if k <= n:
    N = [1]
    for i in range(k):
        while sum(N) <= n:
            N[i] *= 2
        N[i] /= 2

    rest = n - sum(N)

    if rest == 0:
        print(0)
    else:
        answer = int(min(N) - rest)
        print(answer)
else:
    print(-1)




# 11(3) k = 1 / 4
# 1101(13) k = 2 / 8 8
# 10000(16) k = 3 # k보다 1의 숫자가 작은경우 그냥 더하면됨.. , 8 4 4
# 11110(30) k = 2 # k보다 1의 숫자가 큰 경우 한자리 수 더하고 가장 작은 수 100001
# # 524,288 262,144 131,072 65,536 32,768 (1,015,808)

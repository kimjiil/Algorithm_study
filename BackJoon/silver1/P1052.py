# 물병
# 이진법으로 변환했을떄 1의 개수가 k보다 작을 경우

import sys
input = sys.stdin.readline

# n, k = map(int, input().split())

n = int('0b101010101011001000010000', 2)
# n = 3
k = 7
bin_n = bin(n)[2:]
#보다 큰                     '11110000000000000000'

if bin_n.count('1') > k:
    i = 0
    n_k = 0
    while n_k < k:
        if bin_n[i] == '1':
            n_k += 1
        i += 1

    answer = int('0b' + bin_n[:i] + '0' * (len(bin_n) - i), 2) + int('0b' + '1' + '0' *(len(bin_n) - i), 2)
    answer = answer - n
    print(answer)
else:
    print(0)



# 11(3) k = 1 / 4
# 1101(13) k = 2 / 8 8
# 10000(16) k = 3 # k보다 1의 숫자가 작은경우 그냥 더하면됨.. , 8 4 4
# 11110(30) k = 2 # k보다 1의 숫자가 큰 경우 한자리 수 더하고 가장 작은 수 100001
# # 524,288 262,144 131,072 65,536 32,768 (1,015,808)

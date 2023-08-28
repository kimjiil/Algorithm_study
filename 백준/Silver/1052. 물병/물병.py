import sys
input = sys.stdin.readline

n, k = map(int, input().split())

bin_n = bin(n)[2:]

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
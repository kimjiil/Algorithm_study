# 막대기

# 16 4 2 1
# 23 10111

import sys

input = sys.stdin.readline

n = int(input())

print(sum(map(int, list(bin(n)[2:]))))
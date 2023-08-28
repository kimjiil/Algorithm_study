import sys

input = sys.stdin.readline

n = int(input())

print(sum(map(int, bin(n)[2:])))
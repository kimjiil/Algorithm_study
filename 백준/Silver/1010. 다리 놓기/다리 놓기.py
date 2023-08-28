import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    a = 1; b = 1
    for i in range(m, m - n, -1):
        a *= i  # (29, 16)
        b *= (m - i + 1) # 29 - 29 + 1, ... 29 - 17 + 1 0 ~ 12
    print(int(a / b))
    
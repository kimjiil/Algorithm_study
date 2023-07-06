# 제곱 ㄴㄴ 수

# 1 <= min <= 1,000,000,000,000 = 10^12 (10^6)^2
# min <= max <= min + 1,000,000


'''
 1 ~ 10 : 1 2 3 5 6 7 10
 4 9 16 25 36
'''
# 1보다 큰 x의 제곱인 4 <= x^2 <= n에 의해 나누어 떨어지지 않는 수 n을 제곱ㄴㄴ수라고함
# min, max 사이에 있는 수중에 제곱 ㄴㄴ 수의 갯수를 return
import sys
import math

def ver2():
    input = sys.stdin.readline

    min, max = map(int, input().split())

    length = max - min + 1
    prime_array = [True for i in range(int(max ** 0.5) + 1)] # 32
    for i in range(2, len(prime_array) // 2):
        j = i
        while i * j < len(prime_array):
            prime_array[i*j] = False
            j += 1

    prime = []
    for i, t in enumerate(prime_array[2:]):
        if t:
            prime.append(i + 2)

    array = [1] * length # i = 0 => min value 대응

    for p in prime:
        j = int(math.ceil(min / (p ** 2)))
        start = (p ** 2) * j - min
        array[start::(p ** 2)] = [0] * len(array[start::(p ** 2)])

    print(sum(array))

def ver1():
    import sys
    import math

    input = sys.stdin.readline

    min, max = map(int, input().split())

    length = max - min + 1
    array = [True for i in range(length)]

    i = 2
    while i * i <= max:
        j = int(math.ceil(min / (i * i)))
        while i * i * j <= max:
            if array[i * i * j - min]:
                array[i * i * j - min] = False
            j += 1
        i += 1

    print(sum(array))

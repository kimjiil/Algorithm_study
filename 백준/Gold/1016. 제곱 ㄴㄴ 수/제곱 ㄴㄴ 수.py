import sys
import math

inpurt = sys.stdin.readline

min, max = map(int, input().split())

length = max - min + 1
array = [True for i in range(length)]

i = 2
while i*i <= max:
    j = int(math.ceil( min / (i*i) ))
    while i*i * j <= max:
        if array[i*i *j - min]:
            array[i*i*j - min] = False
        j+=1
    i+=1

print(sum(array))

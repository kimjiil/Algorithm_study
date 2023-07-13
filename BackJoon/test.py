
a = [0, 3, 5, 7, 9]

def bs(a, b):
    left = 0
    right = len(a) - 1
    mid = int((left + right) / 2)
    while left < right:
        print(left, mid, right)

        if a[mid] < b:
            left = mid + 1
        else:
            right = mid
        mid = int((left + right) / 2)
    return mid

A = [3, 5, 7, 9, 2, 1, 4, 8]

def solution(A):
    dp = [0]
    b = [0]
    for i, a in enumerate(A):
        if b[-1] < a:
            b.append(a)
            dp.append(dp[-1] + 1)
        else:
            idx = bs(b, a)
            b[idx] = a

    return dp[-1]

solution(A)

# 가장 긴 증가하는 부분 수열 2

'''
왼쪽부터 가장 작은 수를 기준으로 증가하는 수를 count

1 2 3 4 5
2 1 4 5 6 ?
오른쪽에 있는 자신보다 큰 수의 개수
1 5 8 9 2 3 4 5
0 1 2
'''
def solution01():
    '''
    메모리 196640 KB
    시간 3512ms
    '''
    import sys

    input = sys.stdin.readline

    N = int(input())

    seq = map(int, input().split())

    def BinarySearch(a_list, a):
        left = 0
        right = len(a_list) - 1
        mid = int((left + right) / 2)
        while left < right:
            if a_list[mid] < a:
                left = mid + 1
            else:
                right = mid
            mid = int((left + right) / 2)
        return mid

    dp = [0]
    a_list = [0]
    for a in seq:
        if a_list[-1] < a:
            a_list.append(a)
            dp.append(dp[-1] + 1)
        else:
            idx = BinarySearch(a_list, a)
            a_list[idx] = a

    print(dp[-1])

def solution02():
    '''
    메모리 145368 KB
    시간 848ms
    '''
    import sys
    from bisect import bisect_left

    input = sys.stdin.readline

    N = int(input())
    seq = map(int, input().split())
    a_list = [0]

    for a in seq:
        if a_list[-1] < a:
            a_list.append(a)
        else:
            a_list[bisect_left(a_list, a)] = a

    print(len(a_list) - 1)


# 가장 긴 증가하는 부분 수열 5

def solution01():
    '''
    1 <= N <= 1,000,000
    -1,000,000,000 <= A <= 1,000,000,000

    메모리 223700 KB
    시간 1436 ms

    '''


    import sys
    from bisect import bisect_left

    input = sys.stdin.readline

    N = int(input())
    seq = list(map(int, input().split()))

    ########################
    # seq = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    # seq = [2, 8, 9, 5, 6, 7, 1]
    # seq = [3, 5, 7, 9, 2, 1, 4, 8, 9]
    # seq = [3, 5, 6, 9, 2, 1, 4, 7, 8, 9]
    ####################################

    a_list = [-1000000001]
    m_index = [0] # 현재 a_list에 들어있는 값의 index
    # max_seq = [[-1000000001]]
    max_seq_tree = [-1] # 부모 idx를 기록
    for i, a in enumerate(seq):
        if a_list[-1] < a:
            # max_seq.append(max_seq[-1][:])
            # max_seq[-1].append(a)
            a_list.append(a)
            # 현재값의 부모 idx를 넣어야함
            max_seq_tree.append(m_index[-1])
            m_index.append(i + 1)
        else:
            idx = bisect_left(a_list, a)
            a_list[idx] = a
            # max_seq[idx] = max_seq[idx - 1][:]
            # max_seq[idx].append(a)

            max_seq_tree.append(m_index[idx - 1])
            m_index[idx] = i + 1

    from collections import deque
    temp = deque()

    temp.appendleft(a_list[-1])
    i = m_index[-1]
    while max_seq_tree[i] != 0:
        temp.appendleft(seq[max_seq_tree[i] - 1])
        i = max_seq_tree[i]

    print(len(a_list) - 1)
    print(' '.join(map(str, temp)))
    '''
    3 5 7 9 2 1 4 8 9
    3 5 7 8 9
    1 4 7 8 9
    
    3 5 6 9 2 1 4 7 8 9
    3 5 6 7 8 9
    '''

def solution02():
    ''' 맞힌사람 출저
    메모리 221044
    시간 1200ms
    '''
    import sys
    from bisect import bisect_left

    input = sys.stdin.readline

    # N = int(input())
    # seq = list(map(int, input().split()))
    ########################
    seq = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    # seq = [2, 8, 9, 5, 6, 7, 1]
    # seq = [3, 5, 7, 9, 2, 1, 4, 8, 9]
    # seq = [3, 5, 6, 9, 2, 1, 4, 7, 8, 9]
    ####################################
    a_list = []

    tree_idx = []
    for i, a in enumerate(seq):
        if not a_list or a_list[-1] < a:
            a_list.append(a)
            tree_idx.append(len(a_list) - 1)
        else:
            idx = bisect_left(a_list, a)
            a_list[idx] = a
            tree_idx.append(idx)

    answer = len(a_list)

    result = []
    for i in range(len(tree_idx) - 1, -1, -1):
        if tree_idx[i] == answer - 1:
            result.append(seq[i])
            answer -= 1

    print(' '.join(list(map(str, result[::-1]))))
solution02()

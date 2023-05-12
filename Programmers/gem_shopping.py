# [카카오 인턴] 보석 쇼핑
'''

1 <= len(gems) <= 100,000
1 <= len(gems_name) <= 10
'''

import heapq

def solution2(gems):
    gem_name = set(gems)
    n = len(gem_name)
    q = []

    for length in range(n, len(gems) + 1):
        if length == n:
            for i in range(0, len(gems) - length + 1):
                t = set(gems[i:i+length])
                t_l = len(t)
                heapq.heappush(q, (-t_l, i))
                if t_l >= n:
                    return [i+1, i+length]
        else:
            q2 = []
            max_value = 0
            while len(q) > 0:
                involved_char, start_idx = heapq.heappop(q)
                if max_value <= -involved_char:
                    max_value = -involved_char
                    t_l = len(set(gems[slice(start_idx, start_idx+length)]))
                    if t_l >= n:
                        return [start_idx+1, start_idx+length]
                    elif t_l >= max_value:
                        heapq.heappush(q2, (-t_l, start_idx))
                else:
                    break
            q = q2

from collections import defaultdict

# def solution(gems):
#     uniq_gems = set(gems)
#     n_gem = len(uniq_gems)
#     dic = defaultdict(list)
#     for i, k in enumerate(gems):
#         dic[k].append(i)
#
#     # dic_sort = sorted(dic.items(), key= lambda t:len(t[1]))
#     #first_key, first_list = dic_sort.pop(0)
#     first_key, first_list = list(dic.items())[0]
#
#     for length in range(n_gem, len(gems) + 1):
#         for i in first_list:
#             for left, right in zip(range(length,-1, -1), range(0,length+1)):
#                 min = i - left
#                 max = i + right
#                 if min < 0:
#                     min = 0
#
#                 sliced = gems[min:max]
#                 involved_set = len(set(sliced))
#                 if involved_set >= n_gem:
#                     return [min + 1, max]

from collections import defaultdict
import heapq

def solution(gems):
    gem_set = set(gems)
    n_gem_set = len(set(gems))

    gem_dic = defaultdict(int)
    length_heap = []
    start_idx = 0

    for i, gem in enumerate(gems):
        gem_dic[gem] += 1
        end_idx = i
        while n_gem_set <= len(gem_dic):
            heapq.heappush(length_heap, (end_idx - start_idx, (start_idx + 1, end_idx + 1)))

            gem_dic[gems[start_idx]] -= 1
            if gem_dic[gems[start_idx]] == 0:
                del gem_dic[gems[start_idx]]
            start_idx += 1

    return list(length_heap[0][1])



gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
result = [3, 7]
answer = solution(gems)
if result != answer:
    print(answer==result, answer, result)

gems = ["AA", "AB", "AC", "AA", "AC"]
result = [1, 3]
answer = solution(gems)
if result != answer:
    print(answer==result, answer, result)

gems = ["XYZ", "XYZ", "XYZ"]
result = [1, 1]
answer = solution(gems)
if result != answer:
    print(answer==result, answer, result)

gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
result = [1, 5]
answer = solution(gems)
if result != answer:
    print(answer==result, answer, result)

gems = ["a", "b", "c", "d", "e", 'f', 'g', 'h']
result = [1, 8]
answer = solution(gems)
if result != answer:
    print(answer==result, answer, result)

gems = ["a", "b", "c", "d", "e", 'f', 'g', 'g']
result = [1, 7]
answer = solution(gems)
if result != answer:
    print(answer==result, answer, result)
gems = ['a'] * 10
result = [1, 1]
answer = solution(gems)
if result != answer:
    print(answer==result, answer, result)

gems = ['a', 'a', 'b']
result = [2, 3]
answer = solution(gems)
if result != answer:
    print(answer==result, answer, result)

gems = ['1', '2', '1', '2', '1', '2', '1', '3']
result = [6, 8]
answer = solution(gems)
if result != answer:
    print(answer==result, answer, result)

gems = ['1', '1', '2', '3']
result = [2, 4]
answer = solution(gems)
if result != answer:
    print(answer==result, answer, result)

gems = ['1', '1', '1', '2', '2', '2', '3', '3', '3']
result = [3, 7]
answer = solution(gems)
if result != answer:
    print(answer==result, answer, result)

gem_str = '1212121214141414141242442423'
gems = list(gem_str)
result = [19, 28]
answer = solution(gems)
if result != answer:
    print(answer==result, answer, result)
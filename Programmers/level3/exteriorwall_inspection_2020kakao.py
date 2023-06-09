from itertools import permutations, combinations, product

def solution(n, weak, dist):

    dist = sorted(dist, reverse=True)
    n_person = len(dist)

    for n_p in range(1, n_person + 1): #최대 8
        selected_dist = combinations(dist, n_p)
        if len(weak) <= n_p: # 보수할 지점 보다 사람이 많이지는 순간
            return n_p
        selected_wall = combinations(weak, n_p)
        for dist_list in selected_dist:
            for start in selected_wall:
                # unique_comb = []
                permut = permutations(dist_list, len(start))
                for comb in permut:
                    zipped = zip(comb, start)
                    # unique_comb.append(list(zipped))
                    temp = []
                    for d, i in zipped:
                        for _d in range(d + 1):
                            temp.append(divmod(i + _d, n)[1])


                # temp = []
                # for d in dist_list:
                #     for i in start:
                #         for _d in range(d + 1):
                #             temp.append(divmod(i + _d, n)[1])

                if len(set(weak) - set(temp)) == 0:
                    return n_p
    return -1

# if __name__ == '__main__':
#     import ast
#
#     inout_example = '''
#    n	weak	dist	result
# 12	[1, 5, 6, 10]	[1, 2, 3, 4]	2
# 12	[1, 3, 4, 9, 10]	[3, 5, 7]	1
# '''
#     inout_example = inout_example.replace(' ', '')
#     temp = [s for s in inout_example.split('\n') if s != '']
#     key = temp[0].split('\t')
#     for test_case in temp[1:]:
#         args = list(map(ast.literal_eval, test_case.split('\t')))
#         result = args[-1]
#         answer = solution(*args[:-1])
#         print(result, '/', answer)
#
#
# '''
# 1 <= n <= 200
# 1 <= len(weak) <= 15
# 0 <= weak <= n - 1
#
# 1 <= len(dist) <= 8
# 1 <= dist <= 100
# '''
#
import random
for i in range(10):
    random.seed(i)

    n = 12

    n_weak = random.randint(1, 12)
    weak = sorted(random.sample([i for i in range(0, n)], n_weak))
    print('weak - ', weak)
    n_dist = random.randint(1, 8)
    dist = sorted(random.sample([i for i in range(0, n)], n_dist))
    print('dist - ', dist)
    answer = solution(n, weak, dist)
    print(answer)

    print('=' * 20)

n = 20
weak = [1, 6, 12, 17]
dist = [1, 2, 3, 4]
answer = solution(n, weak, dist)
result = 3
print(result,'/', answer)

n = 200
weak = [0, 100]
dist = [1, 1]
answer = solution(n, weak, dist)
result = 2
print(result,'/', answer)

n = 200
weak = [0, 10, 50, 80, 120, 160]
dist = [1, 10, 5, 40, 30]
answer = solution(n, weak, dist)
result = 3
print(result,'/', answer)

n = 16
weak = [1,2,3,4,5,7,8,10,11,12,14,15]
dist = [4,2,1,1]
answer = solution(n, weak, dist)
result = 4
print(result,'/', answer)
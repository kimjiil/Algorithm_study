from itertools import permutations, combinations

'''
 정답은 맞는데 시간 초과남
 
'''
def solution_timelimit(n, weak, dist):

    dist = sorted(dist, reverse=True)
    n_person = len(dist)

    for n_p in range(1, n_person + 1): #최대 8
        selected_dist = combinations(dist, n_p)
        if len(weak) <= n_p: # 보수할 지점 보다 사람이 많이지는 순간
            return n_p
        selected_wall = combinations(weak, n_p)
        for dist_list in selected_dist:
            for start in selected_wall:
                permut = permutations(dist_list, len(start))
                for comb in permut:
                    zipped = zip(comb, start)
                    temp = []
                    for d, i in zipped:
                        for _d in range(d + 1):
                            temp.append(divmod(i + _d, n)[1])


                    if len(set(weak) - set(temp)) == 0:
                        return n_p
    return -1

def valid_weak(start, dist, weak, n):
    end = start + dist
    if end // n > 0:
       if end // n > 1: # 한바퀴 이상을 돈경우
           return weak
       else: # 한바퀴
           if end // n == start - 1: #딱 한바퀴 돌은 경우
               return weak
           else:
               for i in range(len(weak) - 1, -1, -1):
                   if weak[i] < start:
                       w = weak[i] + n
                       if start <= w and w <= end:
                           weak.pop(i)
                   else:
                       if start <= weak[i] and weak[i] <= end:
                           weak.pop(i)
    else:
        for i in range(len(weak) - 1, -1, -1):
            if start <= weak[i] and weak[i] <= end:
                weak.pop(i)


# 최적화 실패 솔루션
def solution_time_limit2(n, weak, dist):
    dist = sorted(dist, reverse=True)
    n_person = len(dist)

    for n_p in range(1, n_person + 1): #최대 8
        selected_dist = combinations(dist, n_p)
        if len(weak) <= n_p: # 보수할 지점 보다 사람이 많이지는 순간
            return n_p
        selected_wall = combinations(weak, n_p)
        for dist_list in selected_dist:
            for start in selected_wall:
                permut = permutations(dist_list, len(start))
                for comb in permut:
                    zipped = sorted(zip(comb, start), key= lambda x: x[0], reverse=True)
                    _weak = weak[:]
                    for d, s in zipped:
                        valid_weak(s, d, _weak, n)
                        if len(_weak) == 0:
                            return n_p
    return -1


'''
    1. 사람수가 적은 case 부터 시작 1, 2, ...
    * 만약 사람수가 커버할 장소와 같아지면 stop
    2. 사람 수 만큼의 dist를 선택
    * 이때 dist는 최대값 정렬을 통해 앞에서부터 순차적으로 선택함, 
        => 사람수가 2명일때 [4, 3]을 선택하게 되는데 이떄 [4, 2] or [4, 1]은 배제함 어차피 3보다 작은수는 3에서 커버가 다됨
    ** 선택된 dist를 permutation을 통해 각 사람에 대한 경우의 수를 모두 구함
        => [4, 3], [3, 4]
    3. 시작점은 모든 n에서 시작할 필요 없이 weak 지점에서 시작하면 된다.
    * 1에서 왼쪽으로 4 가는 것과 10에서 오른쪽으로 4 가는 것은 동일 하기 떄문에 중복을 방지하기 위해
        항상 지점에서 오른쪽으로 가는것으로 한정
        => 첫번째 시작 지점인 1에서 시작하는 경우 list = [1, 5, 6, 10]에서 d = 4일때 커버할 수있는 장소를 list에서 제외함
            list = [6, 10] 이 되고 이떄 다음 시작 지점은 6이됨 
            이렇게 반복해서 list가 비어있는 상태일때의 사람 수를 return 함
            
    4. 모든 경우의 수를 다 탐방했으나 return 되지 않은 경우는 마지막에 -1 return함 
'''
def solution(n, weak, dist):
    dist = sorted(dist, reverse=True)
    n_person = len(dist)

    for n_p in range(1, n_person + 1):
        selected_dist = permutations(dist[:n_p], n_p)
        if len(weak) <= n_p:
            return n_p

        for dist_list in selected_dist: #[4,3], [3, 4]
            for start_i in range(len(weak)):
                start_list = weak[start_i:] + weak[:start_i] #deep copy# i = 0, 1 ...
                # s = start_list[start_i]

                for d in dist_list:
                    s = start_list.pop(0)
                    valid_weak(s, d, start_list, n)

                    if len(start_list) == 0:
                        return n_p

    return -1



if __name__ == '__main__':
    import ast

    inout_example = '''
   n	weak	dist	result
12	[1, 5, 6, 10]	[1, 2, 3, 4]	2
12	[1, 3, 4, 9, 10]	[3, 5, 7]	1
'''
    inout_example = inout_example.replace(' ', '')
    temp = [s for s in inout_example.split('\n') if s != '']
    key = temp[0].split('\t')
    for test_case in temp[1:]:
        args = list(map(ast.literal_eval, test_case.split('\t')))
        result = args[-1]
        answer = solution(*args[:-1])
        print(result, '/', answer)


'''
1 <= n <= 200
1 <= len(weak) <= 15
0 <= weak <= n - 1

1 <= len(dist) <= 8
1 <= dist <= 100
'''

# import random
# for i in range(10):
#     random.seed(i)
#
#     n = 12
#
#     n_weak = random.randint(1, 12)
#     weak = sorted(random.sample([i for i in range(0, n)], n_weak))
#     print('weak - ', weak)
#     n_dist = random.randint(1, 8)
#     dist = sorted(random.sample([i for i in range(0, n)], n_dist))
#     print('dist - ', dist)
#     answer = solution(n, weak, dist)
#     print(answer)
#
#     print('=' * 20)

n = 20
weak = [1, 6, 12, 17]
dist = [1, 2, 3, 4]
answer = solution(n, weak, dist)
result = 3
print(result,'/', answer)

# n = 200
# weak = [0, 100]
# dist = [1, 1]
# answer = solution(n, weak, dist)
# result = 2
# print(result,'/', answer)
#
# n = 200
# weak = [0, 10, 50, 80, 120, 160]
# dist = [1, 10, 5, 40, 30]
# answer = solution(n, weak, dist)
# result = 3
# print(result,'/', answer)
#
# n = 16
# weak = [1,2,3,4,5,7,8,10,11,12,14,15]
# dist = [4,2,1,1]
# answer = solution(n, weak, dist)
# result = 4
# print(result,'/', answer)
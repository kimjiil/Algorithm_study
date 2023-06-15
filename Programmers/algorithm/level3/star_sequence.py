# 스타 수열


'''
x의 길이는 2이상 짝수
x의 길이가 2n일때
{x[0], x[1]} , {x[2], x[3]} , ... , {x[2n-2], x[2n-1]}으로 2개씩 짝지어진 n개의 부분 집합의 교집합은
적어도 1개 이상 되어야 된다.
이때 같은 부분 집합에는 같은 수가 포함되면 안된다.

a의 부분 수열중에서 가장 길이가 긴 스타 수열의 길이를 return
 1<= len(a) <= 500,000
 a의 원소는    0 <= a(i) < len(a)

 (풀이)
 연속으로 있지 않으면서 건너건너 가장 많이 있는 숫자

1) 완전 탐색 a의 범위인 1부터 len(a)까지 공통분모를 설정하고 전체 탐색
    => 최대 탐색 n = 500,000 O(n^2)이 나옴 250,000,000,000 (아마 시간초과 날듯)

2) 가장 많이 있는 숫자부터?
    처음 숫자 카운터 O(n)
    '3333333321242521'
    3 - 8개 / 2 - 4개 /1 - 2개 /4 - 1개 / 5 - 1개
    => 정답은 2개의 개수인 4개..

3) 처음 숫자 카운터때 연속된 숫자들 다삭제?
    '3333333321242521' => 321242521
    3 - 1개 / 2 - 4개 / 1 - 2개 / 4 - 1개 / 5 - 1개
    반례)
    0 2 2 0 => 0 2 0
    연속으로 있는 숫자가 있으면 2개로 줄임 ex 222 -> 22
    0 2 / 2 0 / 2 (2 0) / 0 2 / 2 0 => 0 2 2 0 2 2 0 0 2 2 0  0 - 5개 / 2 - 6개
    그리고 최대값을 가지는 숫자에 대해서 deque로 2개를 가장 많은 숫자가 들어오고 2개면 묶음으로 처리함


'''
from collections import deque, defaultdict
def solution(a):
    a = list(a)
    remove_dup = deque()
    counter = defaultdict(int)
    for s in a: # O(n)
        if len(remove_dup) > 1:
            if remove_dup[-1] != s or remove_dup[-2] != s:
                remove_dup.append(s)
                counter[s] += 1
        else:
            remove_dup.append(s)
            counter[s] += 1

    # O(nlogn)
    counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    max_value = counter[0][1]

    max_answer = 0
    for key, value in counter:
        answer = 0
        if value >= max_value:
            dq = deque()
            for s in remove_dup:
                dq.append(s)
                if len(dq) > 1:
                    if key in dq and dq[0] != dq[1]:
                        answer += 1
                        dq.clear()
                    else:
                        dq.popleft()

            if answer > max_answer:
                max_answer = answer

    return max_answer * 2


if __name__ == '__main__':
    import ast

    inout_example = '''
a	result
[0]	0
[5,2,3,3,5,3]	4
[0,3,3,0,7,2,0,2,2,0]	8
'''
    inout_example = inout_example.replace(' ', '')
    temp = [s for s in inout_example.split('\n') if s != '']
    key = temp[0].split('\t')
    for test_case in temp[1:]:
        args = list(map(ast.literal_eval, test_case.split('\t')))
        result = args[-1]
        answer = solution(*args[:-1])
        print(result, '/', answer)


# 5 2 3 5 3
# 0 3 / 0 7 / 2 0 / 2 0

'''
 0 2 2 0 => 2개..
'''
a = [3,3,3,3,2,3,2,3,2,3,2,3]
answer = solution(a)
result = 8
print(result, '/', answer)

a = list('3333333321242521')
answer = solution(a)
result = 8
print(result, '/', answer)

a =[0, 0, 3, 1, 2, 1, 3, 4, 0, 1, 4]
'''
0 0 3 1 2 1 3 4 0 1 4
0 3개
1 3개
2 
'''
answer = solution(a)
print('test', '/', answer)


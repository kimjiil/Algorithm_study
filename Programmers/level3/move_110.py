# 110 옮기기 (월간 코드 챌린지 시즌2)

from collections import deque

def solution_fail_1(s):
    answer = []


    for string in s:
        cur = []
        left = []
        right = list(string)

        change = True
        # 바뀐게 하나라도 있으면 다시 검사..
        while change:
            change = False
            while len(right) > 0:
                cur.append(right.pop(0))
                if cur == ['1', '1', '0']:
                    while len(right) > 0 and right[0] == '0':
                        left.append(right.pop(0))
                        change = True

                    while len(left) > 0 and left[-1] == '1':
                        right.insert(0, left.pop(-1))
                        change = True
                    break
                    left.append(cur.pop(0))
                elif len(cur) == 3:
                    left.append(cur.pop(0))

            right = left + cur + right
            left = []
            cur = []

        answer.append(''.join(right))
    return answer

from collections import deque

# 최적화 실패 솔루션
def solution_fail_timelimit1(s):
    answer = []

    for string in s:
        n_110 = 0
        cur = deque()
        left = deque()
        right = deque(list(string))
        exist_110 = True
        while exist_110:
            exist_110 = False

            while len(right) > 0:
                cur.append(right.popleft())
                if cur == deque(['1', '1', '0']):
                    n_110 += 1
                    cur.clear()
                    exist_110 = True
                elif len(cur) == 3:
                    left.append(cur.popleft())

            right = left + cur + right
            left = deque()
            cur = deque()

        left = right
        right = deque()

        while len(left) > 0 and left[-1] == '1':
            right.appendleft(left.pop())

        answer.append(''.join((left + deque(['110'] * n_110) + right)))

    return answer

from collections import deque

def solution_fail_timelimit2(s):
    answer = []

    for string in s:
        total_110 = 0
        remain = string.split('110')
        n_110 = len(remain) - 1
        total_110 += n_110
        while n_110 > 0:
            temp = ''.join(remain)
            remain = temp.split('110')
            n_110 = len(remain) - 1
            total_110 += n_110

        remain = list(remain[0])
        right = deque()
        while len(remain) > 0 and remain[-1] == '1':
            right.appendleft(remain.pop())
        answer.append(''.join(remain + ['110'] * total_110 + list(right)))

    return answer

from collections import deque

def solution(s):
    answer = []

    for string in s:
        n_110 = 0
        stack = []
        for char in string:
            if len(stack) > 1 and char == '0' and stack[-2:] == ['1', '1']:
                stack.pop()
                stack.pop()
                n_110 += 1
            else:
                stack.append(char)

        n_1 = 0
        while len(stack) > 0 and stack[-1] == '1':
            stack.pop()
            n_1 += 1

        answer.append(''.join(stack + ['110'] * n_110 + ['1'] * n_1))

    return answer

if __name__ == '__main__':
    import ast

    inout_example = '''
s	result
["1110","100111100","0111111010"]	["1101","100110110","0110110111"]
'''
    inout_example = inout_example.replace(' ', '')
    temp = [s for s in inout_example.split('\n') if s != '']
    key = temp[0].split('\t')
    for test_case in temp[1:]:
        args = list(map(ast.literal_eval, test_case.split('\t')))
        result = args[-1]
        answer = solution(*args[:-1])
        print(result, '/', answer)



s = ['1100']
result = ['0110']
answer = solution(s)
print(result, '/', answer)

'''
110 01 110 1 110 1001
'''

'''
110 01 110 1 110 1001


------------------
 010 110 110 110 110 1


원본 : 
110 01 110 1 110 1001
---------------------
110 110 110 110
010 <> 1

111 - 7
* 110 - 6
101 - 5
100 - 4
011 - 3
010 - 2
001 - 1
000 - 0


--------------------
정답: 
01 0 110 110 110 110 1
'''


s = ["1100111011101001"]
result = ['0101101101101101']
answer = solution(s)
print(result, '/', answer)

for i in range(100, 150):
    s = [str(bin(i))[2:]]

    answer = solution(s)
    print(s, '/', answer)




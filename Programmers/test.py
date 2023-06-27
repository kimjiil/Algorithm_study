
def selection(sticker, i, available, result):
    n = len(sticker)
    available[i % n] = 0
    available[(i - 1) % n] = 0
    available[(i + 1) % n] = 0

    if sum(available) == 0:
        return result + sticker[i]
    temp = []
    for jump in [2, 3]:
        if available[(i + jump) % n]:
            a = selection(sticker, i + jump, available[:], result + sticker[i])
            temp.append(a)

    return max(temp)

def solution(sticker):
    answer = 0

    available = [1] * len(sticker)
    temp = []
    for i in [0, 1]:
        a = selection(sticker, i, available[:], 0)
        temp.append(a)

    return max(temp)


'''
 14 [6] 5 [11] 3 [9] 2 [10]
 
14 
5   /  11
3 9  / 9 2
 
 6 -> 그다음 11 3
'''



if __name__ == '__main__':
    import ast

    inout_example = '''
sticker	answer
[14, 6, 5, 11, 3, 9, 2, 10]	36
[1, 3, 2, 5, 4]	8
'''
    inout_example = inout_example.replace(' ', '')
    temp = [s for s in inout_example.split('\n') if s != '']
    key = temp[0].split('\t')
    for test_case in temp[1:]:
        args = list(map(ast.literal_eval, test_case.split('\t')))
        result = args[-1]
        answer = solution(*args[:-1])
        print(result, '/', answer)
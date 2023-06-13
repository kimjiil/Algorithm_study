# 2023 kakao blind recruit / 표현 가능한 이진 트리

'''
완전 2진 트리의 수는 1, 3, 7, 15
높이 가 h일때 2^h - 1 개

4 ~ 7 3자리
8 ~ 15 4자리

'''


def solution(numbers):
    answer = []

    for n in numbers:
        bi = bin(n)[2:]

        # 자릿수 맞추기
        l = len(bi)
        while len(bi) < 2 ** (len(bin(l)[2:])) - 1:
            bi = '0' + bi

        root_idx = int((len(bi) - 1) / 2)
        # 1일때 0
        # 3일때 root index 1 / 0 (1) 2 / h = 2
        # 7일때 root index 3 / 0 1 2 (3) 4 5 6 / h = 3
        # 15일때 root index 0 1 2 (3) 4 5 6 (7) 8 9 10 (11) 12 13 14  / h = 4

        # root_idx에서 child idx로 이동 7 +- int(2 **(h - 2))

        # child가 1인데 parent가 0이면 valid하지 않음

        h = len(bin(len(bi))[2:])
        node_list = [(root_idx, h)]
        visited = [0 for _ in range(len(bi))]
        visited[root_idx] = 1

        while len(node_list) > 0:
            cur, h = node_list.pop(0)
            left = cur - int(2 ** (h - 2))
            right = cur + int(2 ** (h - 2))
            if (bi[left] == '1' or bi[right] == '1') and bi[cur] == '0':
                answer.append(0)
                break

            h = h - 1
            if visited[right] == 0:
                node_list.append((right, h))
                visited[right] = 1
            if visited[left] == 0:
                node_list.append((left, h))
                visited[left] = 1

        if not 0 in visited:
            answer.append(1)

    return answer



if __name__ == '__main__':
    import ast

    inout_example = '''
numbers	result
[7, 42, 5]	[1, 1, 0]
[63, 111, 95]	[1, 1, 0]
'''
    inout_example = inout_example.replace(' ', '')
    temp = [s for s in inout_example.split('\n') if s != '']
    key = temp[0].split('\t')
    for test_case in temp[1:]:
        args = list(map(ast.literal_eval, test_case.split('\t')))
        result = args[-1]
        answer = solution(*args[:-1])
        print(result, '/', answer)
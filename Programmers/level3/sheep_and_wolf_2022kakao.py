#양과 늑대

def recur_node(current_node, available_nodes, childs, info, sheep, wolf):

    if info[current_node] == 0:
        sheep += 1
    else:
        wolf += 1

    if sheep <= wolf:
        return sheep

    if len(available_nodes) == 0: # 리프 노드 일 경우
        return sheep
    else:
        max_value = 0
        for node in available_nodes:
            sub_nodes = available_nodes[:]
            sub_nodes.remove(node)
            sub_nodes.extend(childs[node])
            value = recur_node(node, sub_nodes, childs, info, sheep, wolf)
            if max_value < value:
                max_value = value
        return max_value

def solution(info, edges):
    answer = 0
    childs = [[] for _ in range(len(info))]

    for parent, child in edges:
        childs[parent].append(child)

    answer = recur_node(0, childs[0], childs, info, 0, 0)
    # 현재 방문중인 노드에서 방문할 수 있는 노드
    return answer

if __name__ == '__main__':
    import ast

    a = '''
    info	edges	result
    [0,0,1,1,1,0,1,0,1,0,1,1]	[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]	5
    [0,1,0,1,1,0,1,0,0,1,0]	[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]	5
    '''
    a = a.replace(' ', '')
    temp = [s for s in a.split('\n') if s != '']
    key = temp[0].split('\t')
    for test_case in temp[1:]:
        args = list(map(ast.literal_eval, test_case.split('\t')))
        result = args[-1]
        answer = solution(*args[:-1])
        print(result, '/', answer)



'''
* 항상 양의수 > 늑대 , 같아지면 잡아먹힘
i )현재 노드 = 0 // 방문 가능한 노드 목록 = [1, 8]
i - 1) 방문 노드 = 1 // 양 2 늑대 0
    방문 가능한 노드 = [2, 4, 8]

i - 2) 방문 노드 = 2 // 양 1 늑대 1 - X
    
'''

def solution(n, k, cmd):
    valid = [dict(idx=i, up=i - 1, down=i + 1, valid=True) for i in range(n)]
    valid[0]['up'] = None
    valid[-1]['down'] = None

    delete = []
    cur = valid[k]

    for c in cmd:
        c = c.split(' ')
        c_type = c[0]
        if c_type == 'D':
            move = int(c[1])
            for i in range(move):
                cur = valid[cur['down']]

        elif c_type == 'U':
            move = int(c[1])
            for i in range(move):
                cur = valid[cur['up']]

        elif c_type == 'C':
            cur['valid'] = False
            delete.append([cur['up'], cur['idx'], cur['down']])
            if cur['down'] == None: #마지막 노드이면
                if cur['up'] != None:
                    cur = valid[cur['up']]
                    cur['down'] = None
            else:
                up = cur['up']
                down = cur['down']
                if up != None:
                    valid[up]['down'] = down
                valid[down]['up'] = up
                cur = valid[down]
        elif c_type == 'Z':
            up, idx, down = delete.pop()
            if up != None:
                valid[up]['down'] = idx
            if down != None:
                valid[down]['up'] = idx
            valid[idx]['down'] = down
            valid[idx]['up'] = up
            valid[idx]['valid'] = True

    answer = ''
    for v in valid:
        if v['valid']:
            answer = answer + 'O'
        else:
            answer = answer + 'X'
    return answer

import heapq as hq
def solution(n, k, cmd):
    max_hq = [-i for i in range(k - 1, -1, -1)]
    min_hq = [i for i in range(k, n)]
    answer = ['O' for i in range(n)]
    stack = []
    for c in cmd:
        c = c.split(' ')
        c_type = c[0]
        if c_type == 'U':
            move = int(c[1])
            for i in range(move):
                hq.heappush(min_hq, -hq.heappop(max_hq))
        elif c_type == 'D':
            move = int(c[1])
            for i in range(move):
                hq.heappush(max_hq, -hq.heappop(min_hq))

        elif c_type == 'C':
            d = hq.heappop(min_hq)
            stack.append(d)
            answer[d] = 'X'
            if len(min_hq) == 0 and len(max_hq) > 0:
                hq.heappush(min_hq, -hq.heappop(max_hq))

        elif c_type == 'Z':
            d = stack.pop()
            answer[d] = 'O'
            if len(min_hq) > 0:
                if min_hq[0] < d:
                    hq.heappush(min_hq, d)
                else:
                    hq.heappush(max_hq, -d)
            else:
                hq.heappush(min_hq, d)

    return ''.join(answer)

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
result = "OOOOXOOO"
answer = solution(n, k, cmd)
print(answer)

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
result = "OOXOXOOO"
answer = solution(n, k, cmd)
print(answer)

n = 3
k = 0
cmd = ["C", "Z", "C", "U 1", "C", "C"]
result = "XXO"
answer = solution(n, k, cmd)
print(answer)


n = 3
k = 2
cmd = ["C", "Z" ,"C", "C"]
result = "OXX"
answer = solution(n, k, cmd)
print(answer)

n = 3
k = 0
cmd = ["C", "Z", "C", "U 1", "C", "C"]
result = "XXX"
answer = solution(n, k, cmd)
print(answer)

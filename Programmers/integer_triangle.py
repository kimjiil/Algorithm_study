
triangle = [[7],
            [3, 8],
            [8, 1, 0],
            [2, 7, 4, 4],
            [4, 5, 2, 6, 5]] # h
result = 30
print(len(triangle))
def solution(triangle):
    previous_result = [0]
    for tri in triangle:
        previous_result = dp_tri(previous_result, tri)
    result = max(previous_result)
    return result

def max_return(a,b):
    if a > b:
        return a
    else:
        return b

def dp_tri(previous_result, tri):
    temp = []
    for idx, p_res in enumerate(previous_result):
        for t in tri[idx:idx+2]:
            temp.append(p_res + t)
    if len(temp) > 3:
        odd_temp = temp[1:-1][1::2]
        even_temp = temp[1:-1][0::2]
        a = list(map(max_return, odd_temp, even_temp))
        temp = temp[0:1] + a + temp[-1:]
    return temp
print(solution(triangle))


'''
    [7] + [3, 8] => [10, 15]
    [10, 15] + [8, 1, 0] => [18, [11, 16], 15] => [18, 16, 15]  // 0 [1 2] 3
    [18, 16, 15] + [2, 7, 4, 4] => [20, [25, 23], [20, 19], 19] => [20, 25, 20, 19] // 0 [1 2] [3 4] 5
    [20, 25, 20, 19] + [4, 5, 2, 6, 5] => [24, [25, 30], [27, 22], [26, 25], 24] => [24, 30, 27, 26, 24] // 0 [1 2] [3 4] [5 6] 7
    result = 30
'''

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]] # h

solution = lambda t, l = []: max(l) if not t else solution(t[1:], [max(x,y)+z for x,y,z in zip([0]+l, l+[0], t[0])])

'''
1st solution t = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
call -> solution( [[3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]], [7] )

2nd solution 
t = [[3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]] 
l = [7]
[0, 7], [7, 0], [3, 8]
i) 0, 7, 3 => max(0, 7) + 3 = 10
ii) 7, 0, 8 => max(7, 0) + 8 = 15
call -> solution( [[8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]], [10, 15])

3rd solution
t = [[8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
l = [10, 15]
[0, 10, 15], [10, 15, 0], [8, 1, 0]
1) max(0, 10) + 8 = 18
2) max(10, 15) + 1 = 16
3) max(15, 0) = 0 = 15
'''
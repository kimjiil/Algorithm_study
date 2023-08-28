def solution(scores):
    answer = 1
    wonho = scores[0]
    
    max_value = 0
    sorted_list = sorted(scores[1:], key=lambda x:(-x[0], x[1]))
    for s in sorted_list:
        if s[0] > wonho[0] and s[1] > wonho[1]:
            return -1

        if sum(s) > sum(wonho):
            if max_value <= s[1]:
                max_value = s[1]
                answer += 1
                
    return answer
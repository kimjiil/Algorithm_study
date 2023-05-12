# 베스트 앨범
'''
장르별로 총 재생횟수로 정렬
장르내에서 재생횟수로 정렬

'''
from collections import defaultdict

def solution(genres, plays):
    t = []
    for i, (g, p) in enumerate(zip(genres, plays)):
        t.append([p, g, i])

    temp = sorted(t, key = lambda t: t[0], reverse=True)

    d = defaultdict(lambda:dict({'p': 0, 'idx': []}))
    for p, g, i in temp:
        d[g]['p'] += p
        d[g]['idx'].append(i)

    d = sorted(d.items(), key=lambda t: t[1]['p'], reverse=True)
    answer = []
    for i in d:
        answer += i[1]['idx'][:2]
    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
result = [4, 1, 3, 0]
answer = solution(genres, plays)
print(answer == result, result, answer)
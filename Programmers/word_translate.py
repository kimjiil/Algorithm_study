# 단어 변환

'''
begin - "hit"
target - "cog"

hit -> hot -> dot -> dog -> cog 4단계

'''


def solution(begin, target, words):
    answer = 0
    words = [begin] + words
    m = [[0 for i in range(len(words))] for i in range(len(words))]

    for i in range(len(words)):
        for j in range(len(words)):
            if i == j:
                m[i][j] = 1
            else:
                if word_diff(words[i], words[j]):
                    m[i][j] = 1

    # target word가 words 집합에 없는 경우 리턴 0
    if not target in words:
        return 0
    else:
        distance = bfs_distance(begin, target, words, m)
    return distance[words.index(target)]

def bfs_distance(begin, target, words, edges):
    start = words.index(begin)
    end = words.index(target)

    distance = [0 for i in range(len(words))]
    visited = [0 for i in range(len(words))]
    queue = [start]
    visited[start] = 1
    while len(queue) > 0:
        idx = queue.pop()
        for i, link in enumerate(edges[idx]):
            if link == 1 and visited[i] == 0 and idx != i: # 인접하고 방문하지 않은 노드
                queue.append(i)
                visited[i] = 1
                distance[i] = distance[idx] + 1

    return distance


def word_diff(word1, word2):
    count = 0
    word1 = list(word1)
    word2 = list(word2)
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1

    if count == 1:
        return True
    else:
        return False



word1 = 'hit'
word2 = 'hot'

print(word_diff(word1, word2))
words = ["hot", "dot", "dog", "lot", "log", "cog"]
target = 'cog'
begin = 'hit'
print(solution(begin, target, words))

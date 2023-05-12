# 불량사용자
import re
from itertools import product

def solution(user_id, banned_id):
    answer = 0
    dic = dict()
    for i, ban in enumerate(banned_id):
        if not ban in dic:
            ban_key = ban
            dic[ban_key] = set()
        else:
            ban_key = ban + f'{i}'
            dic[ban_key] = set()
        for user in user_id:
            if re.match(ban.replace('*', '[0-9a-z]'), user) and len(user) == len(ban):
                dic[ban_key].add(user)

    answer = []
    temp = list(product(*[dic[key] for key in dic]))
    temp = [set(t) for t in temp if len(set(t)) == len(banned_id)]
    temp = set([''.join(t) for t in temp])

    return len(temp)


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]
result = 2
answer = solution(user_id, banned_id)
print(result == answer, answer, result)

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["*rodo", "*rodo", "******"]
result = 2
answer = solution(user_id, banned_id)
print(result == answer, answer, result)

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
result = 3
answer = solution(user_id, banned_id)
print(result == answer, answer, result)
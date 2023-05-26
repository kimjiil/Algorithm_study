# 가장 긴 팰린드롬

def find_pal(length, word):
    for start in range(len(word) - length + 1):
        i = start
        j = start + length - 1
        while j > i:
            if word[i] != word[j]:
                break
            else:
                i += 1
                j -= 1
        if j <= i:
            return True
    return False

def solution(s):
    left = 0
    right = int(len(s) / 2)
    odd_answer = 1

    # 홀수
    while left <= right:
        mid = int((left + right) / 2)
        length = 2 * mid + 1
        if find_pal(length, s):
            odd_answer = length
            left = mid + 1
        else:
            right = mid - 1

    left = 0
    right = int(len(s) / 2)
    even_answer = 1
    # 짝수
    while left <= right:
        mid = int((left + right) / 2)
        length = 2 * mid
        if find_pal(length, s):
            even_answer = length
            left = mid + 1
        else:
            right = mid - 1


    return max(even_answer, odd_answer)
s = "abcdcba"
result = 7
answer = solution(s)
print(answer)

s = "abacde"
result = 3
answer = solution(s)
print(answer)

s = "fghhhdabadcde"
result = 5
answer = solution(s)
print(answer)

s = "f"
result = 1
answer = solution(s)
print(answer)

s = "ff"
result = 2
answer = solution(s)
print(answer)

s = "ffe"
result = 2
answer = solution(s)
print(answer)

s = "effe"
result = 2
answer = solution(s)
print(answer)

s = "abcde"
result = 2
answer = solution(s)
print(answer)
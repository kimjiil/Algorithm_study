import datetime

def solution(today, terms, privacies):
    answer = []
    a = datetime.date.fromisoformat(today.replace('.', '-'))
    b = privacies[0].split(' ')[0].replace('.', '-')
    c = datetime.date.fromisoformat(b)
    datetime.timedelta()
    datetime.date(m)
    return answer

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
result = [1, 3]
answer = solution(today, terms, privacies)
print(answer)

today = "2020.01.01"
terms = ["Z 3", "D 5"]
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
result = [1, 4, 5]
answer = solution(today, terms, privacies)
print(answer)
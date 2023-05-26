from collections import defaultdict
import heapq

def search(use_ticket_index, tickets): # n 사용 티켓 수
    ticket_index = []
    use_ticket = tickets.pop(use_ticket_index) # 사용 티켓 삭제

    start = use_ticket[1]

    if len(tickets) == 0:
        return [[start]]

    for i, ticket in enumerate(tickets):
        if start == ticket[0]:
            ticket_index.append([i, ticket])
    ticket_index = sorted(ticket_index, key=lambda t:t[1])

    if len(ticket_index) == 0 and len(tickets) > 0: # 다음 갈 목적지가 없는데 티켓이 남아있는 경우
         return [[start]]

    route = []
    for i, ticket in ticket_index:
        for t in search(i, tickets[:]):
            route.append([start] + t)

    return route

def solution(tickets):
    start = "ICN"
    ticket_index = []

    for i, ticket in enumerate(tickets):
        if start == ticket[0]:
            ticket_index.append([i, ticket])

    ticket_index = sorted(ticket_index, key=lambda t: t[1])
    route = []
    for i, ticket in ticket_index:
        for t in search(i, tickets[:]):
            route.append([start] + t)

    for r in route:
        if len(tickets) + 1 == len(r):
            best_route = r
            break

    return best_route

    # return route

# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# result = ["ICN", "JFK", "HND", "IAD"]
# answer = solution(tickets)
# print(answer)

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
result = ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
answer = solution(tickets)
print(answer)

tickets = [["ICN", "SFO"], ["SFO", "ICN"], ["ICN", "SFO"],["SFO", "ICN"], ["ICN", "SFO"]]
result = ["ICN", "SFO", "ICN", "SFO", "ICN", "SFO"]
answer = solution(tickets)
print(answer)

tickets = [["ICN", "AAA"], ["ICN", "CCC"], ["CCC", "DDD"], ["AAA", "BBB"], ["AAA", "BBB"], ["DDD", "ICN"], ["BBB", "AAA"]]
result = ["ICN", "CCC", "DDD", "ICN", "AAA", "BBB", "AAA", "BBB"]
answer = solution(tickets)
print(answer)
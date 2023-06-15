# 1차 셔틀 버스
import datetime

def solution(n, t, m, timetable):
    for miniute in range(1, 60*24 + 1):
        bus_tickets = []
        r = []
        for _t in timetable:
            r.append((datetime.time.fromisoformat(_t), 0))

        con_time = (datetime.datetime.min + datetime.timedelta(hours=24, minutes= -miniute)).time()
        r.append((con_time, 1))
        r = sorted(r)

        for i in range(n):
            a = datetime.timedelta(hours=9, minutes=t * i)
            for j in range(m):
                bus_tickets.append((datetime.datetime.min + a).time())

        for ticket in bus_tickets:
            if ticket >= r[0][0]:
                temp = r.pop(0)
                if temp[1] == 1:
                    return temp[0].isoformat(timespec='minutes')


n = 1
t = 1
m = 5
timetable = ["08:00", "08:01", "08:02", "08:03"]
answer = "09:00"
result = solution(n, t, m, timetable)
print(result)

n = 2
t = 10
m = 2
timetable = ["09:10", "09:09", "08:00"]
answer = "09:09"
result = solution(n, t, m, timetable)
print(result)

n = 2
t = 1
m = 2
timetable = ["09:00", "09:00", "09:00", "09:00"]
answer = "08:59"
result = solution(n, t, m, timetable)
print(result)

n = 1
t = 1
m = 5
timetable = ["00:01", "00:01", "00:01", "00:01", "00:01"]
answer = "00:00"
result = solution(n, t, m, timetable)
print(result)


n = 1
t = 1
m = 1
timetable = ["23:59"]
answer = "09:00"
result = solution(n, t, m, timetable)
print(result)

n = 10
t = 60
m = 45
timetable = ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
answer = "18:00"
result = solution(n, t, m, timetable)
print(result)
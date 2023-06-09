# 2021 kakao blind 광고삽입
import datetime


# 첫트라이 시간 초과..
class my_time(object):
    def __init__(self, hour=None, minute=None, second=None):
        if not hour is None:
            object.__setattr__(self, 'hour', hour)
        if not minute is None:
            object.__setattr__(self, 'minute', minute)
        if not second is None:
            object.__setattr__(self, 'second', second)

    def __hash__(self):
        return hash((self.hour, self.minute, self.second))
    def fromstr(self, time_str):
        hour, minute, second = self._get_time(time_str)
        object.__setattr__(self, 'hour', hour)
        object.__setattr__(self, 'minute', minute)
        object.__setattr__(self, 'second', second)

        return self

    def __add__(self, other):
        new_second = self.second + other.second
        new_minute = self.minute + other.minute + new_second // 60
        new_hour = self.hour + other.hour + new_minute // 60

        return my_time(new_hour, new_minute % 60, new_second % 60)

    def __sub__(self, other):
        # self - other
        if self < other:
            raise TypeError
        else:
            new_hour = self.hour - other.hour

            new_minute = self.minute - other.minute
            if new_minute < 0:
                new_minute = 60 + new_minute
                new_hour -= 1

            new_second = self.second - other.second
            if new_second < 0:
                new_second = 60 + new_second
                new_minute -= 1

        return my_time(new_hour, new_minute, new_second)

    def __repr__(self):
        string = str(self.hour) + ':' + str(self.minute).rjust(2, '0') + ':' + str(self.second).rjust(2, '0')
        return string

    def __le__(self, other):
        if other.hour > self.hour:
            return True
        elif other.hour < self.hour:
            return False

        if other.minute > self.minute:
            return True
        elif other.minute < self.minute:
            return False

        if other.second >= self.second:
            return True
        else:
            return False

    def __lt__(self, other):
        if other.hour > self.hour:
            return True
        elif other.hour < self.hour:
            return False

        if other.minute > self.minute:
            return True
        elif other.minute < self.minute:
            return False

        if other.second > self.second:
            return True
        else:
            return False

    def __ge__(self, other):
        if other.hour < self.hour:
            return True
        elif other.hour > self.hour:
            return False
        if other.minute < self.minute:
            return True
        elif other.minute > self.minute:
            return False
        if other.second <= self.second:
            return True
        else:
            return False

    def __gt__(self, other):
        if other.hour < self.hour:
            return True
        elif other.hour > self.hour:
            return False
        if other.minute < self.minute:
            return True
        elif other.minute > self.minute:
            return False
        if other.second < self.second:
            return True
        else:
            return False

    def __eq__(self, other):
        if other.hour == self.hour and other.minute == self.minute and other.second == self.second:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.__eq__(other):
            return False
        else:
            return True
    def _get_time(self, _time):
        hour, minute, second = _time.split(':')
        return int(hour), int(minute), int(second)

    def get_string(self):
        return str(self.hour).rjust(2,'0') +':' + str(self.minute).rjust(2, '0') + ':' + str(self.second).rjust(2, '0')

def solution(play_time, adv_time, logs):
    answer = ''
    insert_times = set()
    insert_times.add(my_time(0,0,0))
    for log in logs:
        t = log.split('-')
        insert_times.add(my_time().fromstr(t[0]))
        insert_times.add(my_time().fromstr(t[1]))

    insert_times = sorted(insert_times)

    adv_duration = my_time().fromstr(adv_time)
    max_play = my_time(0,0,0)
    fast_insert = my_time(99,59,59)
    for insert_time in insert_times:
        adv_start = insert_time
        adv_end = adv_start + adv_duration
        cum_play = my_time(0, 0, 0)
        for log in logs:
            s, e = log.split('-')
            s = my_time().fromstr(s)
            e = my_time().fromstr(e)

            if adv_end < s or e < adv_start:
                pass
            else:
                if s < adv_start:
                    inter_start = adv_start
                else:
                    inter_start = s

                if e < adv_end:
                    inter_end = e
                else:
                    inter_end = adv_end

                inter_duration = inter_end - inter_start
                cum_play = cum_play + inter_duration

        if max_play < cum_play:
            max_play = cum_play
            fast_insert = insert_time
    return fast_insert.get_string()


'''
    시청 기록을 변화율로 저장했다가 dp에서 누적합으로 최대 누적시간 구함
    dp[0] -> 00:00:00 - 00:14:15 사이의 광고 누적 시간
'''
def get_index(str_time):
    h,m,s = get_hms(str_time)
    return 3600 * h + 60 * m + s

def index_to_str(idx):
    h = idx // 3600
    idx = idx - 3600 * h
    m = idx // 60
    idx = idx - 60 * m
    s = idx

    return str(h).rjust(2, '0') +':' + str(m).rjust(2, '0') + ':' + str(s).rjust(2, '0')
def get_hms(str_time):
    h,m,s = str_time.split(':')
    return int(h), int(m), int(s)

def solution(play_time, adv_time, logs):

    time_maps = [0 for _ in range(get_index(play_time))] + [0]

    for log in logs:
        s, e = log.split('-')
        # print(get_index(s), get_index(e))
        time_maps[get_index(s)] += 1
        time_maps[get_index(e)] -= 1

    print()
    for i in range(get_index(play_time)):
        time_maps[i + 1] = time_maps[i + 1] + time_maps[i]
        # print(index_to_str(i), '-  ', time_maps[i + 1])

    dp = [0 for _ in range(get_index(play_time) - get_index(adv_time) + 1)]
    dp[0] = sum(time_maps[0:get_index(adv_time)])

    dp_max = dp[0]
    start_adv_i = 0
    for i in range(1, get_index(play_time) - get_index(adv_time) + 1):
        dp[i] = dp[i - 1] + time_maps[i + get_index(adv_time) - 1] - time_maps[i - 1]
        # 이부분에서 time_map index랑 dp index랑 헷갈렷음
        if dp[i] > dp_max:
            dp_max = dp[i]
            start_adv_i = i

    return index_to_str(start_adv_i)



play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
result = "01:30:59"
answer = solution(play_time, adv_time, logs)
print(answer)

play_time = "99:59:59"
adv_time = "25:00:00"
logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
result = "01:00:00"
answer = solution(play_time, adv_time, logs)
print(answer)

play_time = "50:00:00"
adv_time = "50:00:00"
logs = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]
result = "00:00:00"
answer = solution(play_time, adv_time, logs)
print(answer)

play_time = "00:01:00"
adv_time = "00:00:10"
logs = ["00:00:00-00:00:09", "00:00:10-00:00:20"]
result = "00:00:10"
answer = solution(play_time, adv_time, logs)
print(answer)

import sys

N = int(sys.stdin.readline());
times = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

times = sorted(times, key=lambda x:x[0])
times = sorted(times, key=lambda x:x[1])

end = 0;

cnt = 0
for t in times:
    if end <= t[0]:
        end = t[1]
        cnt +=1
            
print(cnt)
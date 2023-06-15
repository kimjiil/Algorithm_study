

def move(x, y, place, distance, visited):

    visited.append((x, y))
    up = down = left = right = 99
    if place[y][x] == 'O':
        #move
        if y - 1 >= 0 and not (x, y - 1) in visited:
            up = move(x, y - 1, place, distance + 1, visited[:])

        if y + 1 < 5 and not (x, y + 1) in visited:
            down = move(x, y + 1, place, distance + 1, visited[:])

        if x - 1 >= 0 and not (x - 1, y) in visited:
            left = move(x - 1, y, place, distance + 1, visited[:])

        if x + 1 < 5 and not (x + 1, y) in visited:
            right = move(x + 1, y, place, distance + 1, visited[:])

        return min(up, down, left, right)

    elif place[y][x] == 'X':
        return 99
    elif place[y][x] == 'P':
        return distance

def find_P(place, start):
    x, y = start
    visited = [(x, y)]
    up = down = left = right = 99
    if y - 1 >= 0:
        up = move(x, y - 1, place, 1, visited[:])

    if y + 1 < 5:
        down = move(x, y + 1, place, 1, visited[:])

    if x - 1 >= 0:
        left = move(x - 1, y, place, 1, visited[:])

    if x + 1 < 5:
        right = move(x + 1, y, place, 1, visited[:])

    return min(up, down, left, right)

def solution(places):
    answer = [1 for i in range(len(places))]
    for idx, place in enumerate(places):
        #find start
        for y in range(5):
            for x in range(5):
                if place[y][x] == "P":
                    if find_P(place, (x, y)) <= 2:
                        answer[idx] = 0

    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
result = [1, 0, 1, 1, 1]
answer = solution(places)
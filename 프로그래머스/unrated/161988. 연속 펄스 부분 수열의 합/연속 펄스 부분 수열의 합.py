def solution(sequence):
    dp = []
    for i, s in enumerate(sequence):
        if i == 0:
            dp.append(((-1) ** i) * s)
        else:
            dp.append(dp[-1] + ((-1) ** i) * s)

    dp_max = abs(max(dp) - min(min(dp), 0))
    dp_min = abs(min(dp) - max(max(dp), 0))
    return max(dp_max,dp_min)
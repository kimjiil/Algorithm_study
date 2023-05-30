from collections import defaultdict

def solution(enroll, referral, seller, amount):

    idx_dict = defaultdict()
    for i, e in enumerate(enroll):
        idx_dict[e] = i

    benefits = [0 for i in range(len(enroll) + 1)]
    ref_idx = [idx_dict[r] if r != "-" else -1 for r in referral]
    for s, b in zip(seller, amount):
        current_benefit = b * 100
        current_idx = idx_dict[s]

        while current_idx >= 0 and current_benefit > 0:
            benefits[current_idx] += current_benefit - int(current_benefit * 0.1)
            current_benefit = int(current_benefit * 0.1)
            current_idx = ref_idx[current_idx]

    return benefits[:-1]


enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
result = [360, 958, 108, 0, 450, 18, 180, 1080]
answer = solution(enroll, referral, seller, amount)
print(answer)

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["sam", "emily", "jaimie", "edward"]
amount = [2, 3, 5, 4]
result = [0, 110, 378, 180, 270, 450, 0, 0]
answer = solution(enroll, referral, seller, amount)
print(answer)
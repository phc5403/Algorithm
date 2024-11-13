from sys import stdin

N, M = map(int, stdin.readline().split())

dice = {}

for n in range(1, N + 1):
    for m in range(1, M + 1):
        sum_number = n + m

        if sum_number in dice:
            dice[sum_number] += 1
        else:
            dice[sum_number] = 1

max_number = max(dice.values())
res = sorted([k for k, v in dice.items() if v == max_number])
print(*res, sep='\n')

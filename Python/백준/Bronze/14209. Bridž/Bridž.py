from sys import stdin

N = int(stdin.readline())

res = 0
score = {
    'A': 4,
    'K': 3,
    'Q': 2,
    'J': 1,
    'X': 0
}

for _ in range(N):
    cards = list(stdin.readline().strip())

    for card in cards:
        res += score[card]

print(res)
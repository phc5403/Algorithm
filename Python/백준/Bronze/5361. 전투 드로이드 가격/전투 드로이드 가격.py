from sys import stdin


TC = int(stdin.readline())

# parts = {
#     'A': 350.34,
#     'B': 230.90,
#     'C': 190.55,
#     'D': 125.30,
#     'E': 180.90
# }

parts = [350.34, 230.90, 190.55, 125.30, 180.90]

for tc in range(1, TC + 1):
    lst = list(map(int, stdin.readline().split()))
    res = 0

    for part in range(5):
        res += parts[part] * lst[part]

    print(f'${res:.2f}')

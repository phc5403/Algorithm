from sys import stdin


def mission():
    for c in range(M):
        escape = True

        for r in range(N):
            if lst[r][c] == 'O':
                escape = False
                continue

        if escape:
            return c + 1

    return "ESCAPE FAILED"


N, M = map(int, stdin.readline().split())
lst = [list(stdin.readline().strip()) for _ in range(N)]
print(mission())

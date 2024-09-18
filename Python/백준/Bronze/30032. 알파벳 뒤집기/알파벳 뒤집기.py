from sys import stdin


N, D = map(int, stdin.readline().split())

for _ in range(N):
    string = stdin.readline().strip()
    res = ''

    for idx in range(N):
        if D == 1:
            if string[idx] == 'd':
                res += 'q'
            elif string[idx] == 'b':
                res += 'p'
            elif string[idx] == 'q':
                res += 'd'
            else:
                res += 'b'

        elif D == 2:
            if string[idx] == 'd':
                res += 'b'
            elif string[idx] == 'b':
                res += 'd'
            elif string[idx] == 'q':
                res += 'p'
            else:
                res += 'q'

    print(res)
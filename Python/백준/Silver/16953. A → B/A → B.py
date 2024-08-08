from sys import stdin


def dfs(num, cnt):
    global A, B, flag

    if num == B:
        flag = True
        print(cnt + 1)
        return

    if num > B:
        return

    else:  # num <= B
        dfs(num * 2, cnt + 1)
        dfs(int(str(num) + "1"), cnt + 1)


A, B = map(int, stdin.readline().split())
flag = False
dfs(A, 0)

if not flag:
    print(-1)
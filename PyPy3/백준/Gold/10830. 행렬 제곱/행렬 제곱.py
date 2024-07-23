from sys import stdin

N, B = map(int, stdin.readline().split())
lst = [list(map(int, stdin.readline().split())) for _ in range(N)]


def mul(arr, arr2):  # temp * lst (%1000)
    tmp = [[0] * N for _ in range(N)]

    for x in range(N):
        for y in range(N):
            for z in range(N):
                # print(f"result[{x}][{y}] += {arr2[x][z]} * {lst[z][y]}")
                tmp[x][y] += (arr[x][z] * arr2[z][y])

    for a in range(N):
        for b in range(N):
            tmp[a][b] = tmp[a][b] % 1000

    return tmp


def solve(mat, b):  # 지수 처리
    if b == 1:  # 1제곱 = 행렬 원형에 % 처리만.
        for x in range(N):
            for y in range(N):
                mat[x][y] = mat[x][y] % 1000
        return mat

    else:
        if b % 2:  # 지수 = 홀수
            res = solve(mat, b-1)
            return mul(res, lst)

        else:  # 지수 = 짝수
            res = solve(mat, b//2)
            return mul(res, res)


for i in solve(lst, B):
    print(*i)

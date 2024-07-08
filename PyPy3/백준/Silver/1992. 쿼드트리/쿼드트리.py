from sys import stdin
# from pprint import pprint

N = int(stdin.readline())

lst = [list(map(int, stdin.readline().strip())) for _ in range(N)]
res = ""
# pprint(lst)


def div_conq(x, y, n):  # 0 0 8
    global res
    cnt = 0

    for i in range(x, x+n):
        for j in range(y, y+n):
            if lst[i][j]:
                cnt += 1

    if not cnt:  # 현재 영역이 모두 0 -> 압축=0
        res += "0"

    elif cnt == n*n:  # 현재 영역이 모두 1 -> 압축=1
        res += "1"

    else:  # 순차적 필수
        res += "("
        div_conq(x, y, n//2)  # 왼쪽 위
        div_conq(x, y+(n//2), n//2)  # 오른쪽 위
        div_conq(x+(n//2), y, n//2)  # 왼쪽 아래
        div_conq(x+(n//2), y+(n//2), n//2)  # 오른쪽 아래
        res += ")"

    return


div_conq(0, 0, N)
print(res)



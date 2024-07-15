from sys import stdin, stdout
from collections import deque
from pprint import pprint


def width_candy():  # 행 단위 검사
    global res

    for idx in range(N):  # 0 1 2
        temp = 1
        for a, b in zip(board[idx], board[idx][1:]):
            if a == b:
                temp += 1
                res = max(res, temp)
            else:
                temp = 1


def height_candy():  # 열 단위 검사
    global res

    temp = 0

    for a in range(N):
        temp = 1
        tmp = []
        for b in range(N):
            tmp.append(board[b][a])

        for c, d in zip(tmp, tmp[1:]):
            if c == d:
                temp += 1
                res = max(res, temp)
            else:
                temp = 1



# 문제에서 따로 조건은 없지만 <교환은 1번만> 이루어지는것 같음.
N = int(stdin.readline())

board = [list(stdin.readline().strip()) for _ in range(N)]

res = 0

# pprint(board, width=30)

for x in range(N):
    for y in range(N):
        if (y+1) >= N:
            continue

        if board[x][y] != board[x][y+1]:  # 행
            board[x][y], board[x][y+1] = board[x][y+1], board[x][y]
            width_candy()
            height_candy()
            board[x][y], board[x][y+1] = board[x][y+1], board[x][y]

        if (x+1) >= N:
            continue
        if board[x][y] != board[x+1][y]:  # 열
            board[x][y], board[x+1][y] = board[x+1][y], board[x][y]
            width_candy()
            height_candy()
            board[x][y], board[x+1][y] = board[x+1][y], board[x][y]


print(res)



from sys import stdin
from pprint import pprint
from collections import deque
import time


def must_i_turn(second, direction):

    for i, j in operation:
        if second == int(i):
            if j == 'D':  # 오90
                direction = (direction + 1) % 4
            else:  # 왼90
                direction = (direction + 3) % 4
    return direction


def bfs():
    qu = deque()
    cnt = 0  # 게임 시간
    qu.append([0, 0, 1])

    # 뱀의 몸 부분 좌표 저장용.
    snake_body = deque()
    snake_body.append([0, 0])  # 처음 뱀의 몸통.
    board[0][0] = 1

    while qu:  # 처음 방향(cur) = 1(→)
        qulen = len(qu)

        for _ in range(qulen):
            # 머리, 꼬리, 머리 방향
            hx, hy, head = qu.popleft()

            # 방향 바꿔야하는지 확인
            head = must_i_turn(cnt, head)
            nhx = hx + dx[head]
            nhy = hy + dy[head]

            # 종료 1: 다음 방향 이동 시 맵 밖으로 넘어감.
            if 0 > nhx or nhx > N-1 or 0 > nhy or nhy > N-1:
                print(cnt + 1)
                return

            # 종료 2: 자신의 몸과 부딪힘.
            elif board[nhx][nhy] == 1:
                print(cnt + 1)
                return

            # 진행 1: 다음칸 이동 가능.
            if 0 <= nhx < N and 0 <= nhy < N:
                # 사과 X
                if not board[nhx][nhy]:
                    # 뱀 꼬리 끝 부분 뽑아서
                    tx, ty = snake_body.popleft()
                    # 맵 갱신
                    board[tx][ty] = 0

                # 사과를 만났든 말든 어쨌든 뱀의 몸 길이 증가
                snake_body.append([nhx, nhy])  # 뱀의 몸통 추가
                board[nhx][nhy] = 1
                qu.append([nhx, nhy, head])

        cnt += 1


# 2 <= N <= 100
# 1 second, 128 MB
N = int(stdin.readline())
apple = [list(map(int, stdin.readline().split())) for _ in range(int(stdin.readline()))]
board = [[0] * N for _ in range(N)]
operation = [list(stdin.readline().split()) for _ in range(int(stdin.readline()))]

start = time.time()  ##

# 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 0 = 길, * = 사과
for row, col in apple:
    board[row-1][col-1] = '*'

bfs()

end = time.time()  ##
# print(f"{round(int(end - start) * 1000)} ms")

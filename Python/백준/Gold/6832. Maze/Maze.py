from sys import stdin
from collections import deque
from pprint import pprint


# 다음 좌표가 미로의 범위를 벗어나는지 체크
def is_in(nx, ny):
    if 0 <= nx < R and 0 <= ny < C:
        return True
    return False


# 다음 좌표가 이동 가능 + 방문 안한 곳인지 체크
def next_position(nx, ny):
    global visited
    if is_in(nx, ny) and not visited[nx][ny]:
        return True
    return False


# 미로 탐색 함수
def bfs():
    qu = deque([[0, 0, 1]])
    visited[0][0] = True

    while qu:
        x, y, cnt = qu.popleft()

        # END : 종료 조건
        if [x, y] == [R - 1, C - 1]:
            return cnt

        # 1. 4방향 교차로
        if lst[x][y] == '+':
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if next_position(nx, ny) and lst[nx][ny] != '*':
                    visited[nx][ny] = True
                    qu.append([nx, ny, cnt + 1])

        # 2. 세로 방향 교차로
        elif lst[x][y] == '|':
            for k in range(2):
                nx = x + dx[k]
                ny = y + dy[k]

                if next_position(nx, ny) and lst[nx][ny] != '*':
                    visited[nx][ny] = True
                    qu.append([nx, ny, cnt + 1])

        # 3. 가로 방향 교차로
        elif lst[x][y] == '-':
            for k in range(2, 4):
                nx = x + dx[k]
                ny = y + dy[k]

                if next_position(nx, ny) and lst[nx][ny] != '*':
                    visited[nx][ny] = True
                    qu.append([nx, ny, cnt + 1])

    return -1


TC = int(stdin.readline())

for tc in range(1, TC + 1):
    R = int(stdin.readline())
    C = int(stdin.readline())
    lst = [list(stdin.readline().strip()) for _ in range(R)]

    visited = [[False] * C for _ in range(R)]

    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    res = bfs()

    print(res)

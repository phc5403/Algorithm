from sys import stdin, stdout
from collections import deque
from pprint import pprint


def turn(t_x, t_y, t_d):  # 왼쪽으로 회전하기
    if t_d == 0:  # 북 -> 서
        # t_y -= 1
        # t_d = 3
        return t_x, t_y - 1, t_d + 3
    elif t_d == 1:  # 동 -> 북
        # t_x -= 1
        # t_d = 0
        return t_x - 1, t_y, t_d - 1
    elif t_d == 2:  # 남 -> 동
        # t_y += 1
        # t_d = 1
        return t_x, t_y + 1, t_d - 1
    elif t_d == 3:  # 서 -> 남
        # t_x += 1
        # t_d = 2
        return t_x + 1, t_y, t_d - 1


def back_turn(b_x, b_y, b_d):
    # 후진(b_d) = 북 동 남 서
    # back_x = [1, 0, -1, 0]
    # back_y = [0, -1, 0, 1]

    if b_d == 0:
        return b_x + 1, b_y, b_d
    elif b_d == 1:
        return b_x, b_y - 1, b_d
    elif b_d == 2:
        return b_x - 1, b_y, b_d
    elif b_d == 3:
        return b_x, b_y + 1, b_d


def bfs(s_x, s_y, s_d):
    qu = deque()
    qu.append([s_x, s_y, s_d])
    lst[s_x][s_y] = 2

    back_flag = False  # 후진 판단값(초기값 = 불가능한 상태)
    cnt = 1

    while qu:
        x, y, d = qu.popleft()  # 현재 내가 정면 보는 방향
        # print(f'X={x}, Y={y}, D={d}')
        bx, by, bd = back_turn(x, y, d)

        for k in range(4):
            nx, ny, nd = turn(x, y, d)

            if k == 3 and lst[nx][ny]:  # 마지막 방향마저 청소를 못하는 곳이면.
                back_flag = True  # 이제 후진해야하니까 후진 ON

            # print(f'NX,NY,ND = {nx, ny, nd}')

            # 왼쪽 방향을 청소하지 안았다면.
            if not lst[nx][ny]:
                # print("IF")
                lst[nx][ny] = lst[x][y] + 1
                cnt += 1
                qu.append([nx, ny, nd])
                break

            # (후진 전) 4방향 모두 청소할곳 없는지를 판단
            elif lst[nx][ny] and not back_flag:
                # print("ELIF_1")
                d = nd
                continue

            # 4방향 모두 청소해서 갈 수 없다 + 뒤에 벽이 아니면 후진
            elif lst[nx][ny] and lst[bx][by] != 1 and back_flag:
                qu.append([bx, by, bd])
                back_flag = False  # 후진했으니 다시 OFF

            # 4방향 모두 청소해서 갈 수 없다 + 뒤에도 벽이라 못 간다.
            elif lst[nx][ny] and lst[bx][by] == 1 and back_flag:
                back_flag = False


    # pprint(lst, width=50)
    return cnt


N, M = map(int, stdin.readline().split())

# 북=0, 동=1, 남=2, 서=3
start_x, start_y, direction = map(int, stdin.readline().split())

lst = [list(map(int, stdin.readline().split())) for _ in range(N)]

# pprint(lst, width=60)

print(bfs(start_x, start_y, direction))


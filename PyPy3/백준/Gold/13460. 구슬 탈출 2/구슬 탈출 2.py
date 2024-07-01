from sys import stdin
import copy
import time

# 제출 번호 56512439 정답 후, 주석을 추가한 코드 #


# 각 구슬이 Hole에 빠졌는지 판단
def check_hole(nrx, nry, nbx, nby):
    flag_r, flag_b = False, False

    if [nrx, nry] == [hx, hy]:
        flag_r = True

    if [nbx, nby] == [hx, hy]:
        flag_b = True

    return flag_r, flag_b


def move_beaz(rx, ry, bx, by, k):
    global board, hx, hy

    crx, cry, cbx, cby = rx, ry, bx, by
    rmove, bmove = True, True  # 각 구슬이 움직일 수 있는지 여부

    # 각 구슬을 끝까지 이동 시켰을 때, 구슬 하나의 움직임 결과에 따라서
    # 다른 구슬이 또 이동해야할 수 있기 때문에 이중 whlie.
    while rmove or bmove:
        while rmove or bmove:
            # "RED"
            if board[crx + dx[k]][cry + dy[k]] == '.':
                if board[crx][cry] == 'R':
                    board[crx][cry] = '.'
                    crx = crx + dx[k]
                    cry = cry + dy[k]
                    board[crx][cry] = 'R'
                    rmove = True
                else:  # RED in Hole
                    rmove = False

            else:  # 'O' or 'B' or '#'
                if board[crx + dx[k]][cry + dy[k]] == 'O':
                    board[crx][cry] = '.'
                    crx = crx + dx[k]
                    cry = cry + dy[k]
                    rmove = False
                else:  # 'B' or '#'
                    rmove = False

            # "BLUE"
            if board[cbx + dx[k]][cby + dy[k]] == '.':
                if board[cbx][cby] == 'B':
                    board[cbx][cby] = '.'
                    cbx = cbx + dx[k]
                    cby = cby + dy[k]
                    board[cbx][cby] = 'B'
                    bmove = True
                else:  # BLUE in Hole
                    bmove = False

            else:  # 'O' or 'R' or '#'
                if board[cbx + dx[k]][cby + dy[k]] == 'O':
                    board[cbx][cby] = '.'
                    cbx = cbx + dx[k]
                    cby = cby + dy[k]
                    bmove = False
                else:  # 'R' or '#'
                    bmove = False

        # Ex) #RB..# + 오른쪽 이동
        # while 한 번 이동이 끝나면 #R..B# 이 되므로
        # R은 처음과달리 전방이 뚫려버려서 끝까지 더 이동해야하는 경우가 생김.
        if board[crx][cry] == 'R' and board[crx + dx[k]][cry + dy[k]] == '.':
            rmove = True
        if board[cbx][cby] == 'B' and board[cbx + dx[k]][cby + dy[k]] == '.':
            bmove = True

    # 모든 구슬 이동 후의 옮겨간 좌표를 반환
    return crx, cry, cbx, cby


def bfs(rx, ry, bx, by, prev_di, cnt):
    global board, hx, hy, RED, BLUE, res

    if cnt > 10:
        return  # 'None'

    for nxt_di in range(4):
        temp = copy.deepcopy(board)

        # 이전에 갔던 방향은 이미 전진이 더이상 안되는 방향이므로,
        # 다시 같은 방향을 갈 필요가 없음.
        if prev_di == nxt_di:
            continue

        # 불필요한 왔다갔다 방지
        else:  # prev_di != nxt_di
            # 1. 이전 방향과 다음 방향이 상-하 / 좌-우 방지.
            if prev_di % 2 == 0 and prev_di + 1 == nxt_di:
                continue

            # 맨 처음 bfs()에선 prev_di = -1 이라서 (% 2)가 홀수로 나오는데,
            # 2번째 조건이 False라서 통과 못하게끔 함으로써 예외 방지.
            elif prev_di % 2 == 1 and prev_di - 1 == nxt_di:
                continue

            else:
                # move_beaz()의 호출 횟수를 최소화 == O(n) 최소화
                nrx, nry, nbx, nby = move_beaz(rx, ry, bx, by, nxt_di)

                # 구슬 이동 후 바로 홀 여부 판단
                RED, BLUE = check_hole(nrx, nry, nbx, nby)

                # 최대 10번 이하로 움직여야 하면서 +
                if cnt <= 10:
                    # 1. 빨간 구슬만 골인함(정답)
                    if RED and not BLUE:
                        res = min(res, cnt)
                        return

                    # 2. 둘 다 골인 못하면 다음 bfs()에서 계속 진행.
                    elif not RED and not BLUE:
                        bfs(nrx, nry, nbx, nby, nxt_di, cnt + 1)

        board = copy.deepcopy(temp)  # 해당 구문 위치(백업 시키는 타이밍) 중요함.


# 2 second / 512 MB  -> 최대 CASE 2억 미만으로,,
N, M = map(int, stdin.readline().split())

board = []
for _ in range(N):
    board.append(*[list(stdin.readline().strip())])

# start = time.time()  #

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
R, B, H = 0, 0, 0  # Red, Blue, Hole
RED, BLUE = False, False  # 각 구슬이 홀에 빠졌는지 판단
res = 11  # 초깃값 = 정답 조건 10 + 1 = 11번

# 초기 구슬, 홀 좌표 찾기
for row in range(1, N-1):
    for col in range(1, M-1):
        if board[row][col] == 'R':
            R = [row, col]  # [3, 1] / [1, 4]
            # rx, ry = row, col
        if board[row][col] == 'B':
            B = [row, col]  # [1, 3] / [1, 5]
            # bx, by = row, col
        if board[row][col] == 'O':
            # H = [row, col]  # [3, 2] / [5, 1]
            hx, hy = row, col

bfs(R[0], R[1], B[0], B[1], -1, 1)

if 0 < res < 11:  # 1. res가 10번 이하로 정상적으로 성공한 경우
    print(res)
else:             # 2. 10번 이하로 성공 못한 경우 res =초깃값 11이므로 실패 한 경우
    print(-1)

# end = time.time()  #
# print(f'{end - start:.3f} sec')  #

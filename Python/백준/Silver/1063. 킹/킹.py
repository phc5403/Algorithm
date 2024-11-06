from sys import stdin
from collections import deque
from pprint import pprint


# 체스판을 벗어나는지 확인
def is_in(x, y):
    if 0 <= x < 8 and 0 <= y < 8:
        return True
    else:
        return False


# 우 좌 하 상 우상 좌상 우하 좌하
# R  L  B  T  RT   LT   RB   LB
dx = [0, 0, 1, -1, -1, -1, 1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

#

# 주어진 입력을 dx, dy로 치환하기 위한 방향값
directions = {
    'R': 0,
    'L': 1,
    'B': 2,
    'T': 3,
    'RT': 4,
    'LT': 5,
    'RB': 6,
    'LB': 7
}

king, stone, N = stdin.readline().strip().split()  # 입력

dist = deque()  # 입력으로 주어지는 이동값
for _ in range(int(N)):
    dist.append(directions[stdin.readline().strip()])

lst = [[0] * 8 for _ in range(8)]  # 체스판

res = [[], []]

# 1. 시작 좌표 변환(A ~ H -> 65 ~ 72)
king_x, king_y = 8 - int(king[1]), ord(king[0]) - 65
stone_x, stone_y = 8 - int(stone[1]), ord(stone[0]) - 65

# 2. 체스판에 표시(king = 1, stone = 2)
lst[king_x][king_y] = 1
lst[stone_x][stone_y] = 2

qu = deque([[king_x, king_y]])

while dist:
    x, y = qu.popleft()

    k = dist.popleft()
    nx = x + dx[k]
    ny = y + dy[k]

    # 1. 킹의 다음 위치 계산
    if is_in(nx, ny):
        # 2. 이동 경로에 돌이 있을 경우
        if lst[nx][ny] == 2:
            # 2-1. 돌을 옮길 수 있는 경우 -> 위치 갱신
            if is_in(stone_x + dx[k], stone_y + dy[k]):
                lst[stone_x][stone_y] = 0
                lst[stone_x + dx[k]][stone_y + dy[k]] = 2
                stone_x += dx[k]  # 돌 위치 이동
                stone_y += dy[k]
                lst[x][y] = 0  # 킹 위치 이동
                lst[nx][ny] = 1
                qu.append([nx, ny])
            else:  # 2-2. 돌을 옮길 수 없는 경우 -> 건너뜀
                qu.append([x, y])
                continue

        elif lst[nx][ny] == 0:
            lst[x][y] = 0  # 킹 위치 이동
            lst[nx][ny] = 1
            qu.append([nx, ny])

    else:
        qu.append([x, y])

for r in range(8):
    for c in range(8):
        if lst[r][c] == 1:
            temp = ""
            temp += chr(c + 65)
            temp += str(8 - r)
            res[0] = temp
        if lst[r][c] == 2:
            temp = ""
            temp += chr(c + 65)
            temp += str(8 - r)
            res[1] = temp

print(*res, sep='\n')

'''
1. 문제에서 주어진 8방향 탐색.
2. 킹이 이동하는 경로에 돌이 있다면 해당 방향으로 돌을 한 칸 밀어냄.
3. 이동 시 킹 or 돌이 범위 밖 -> 해당 이동 건너 뜀.
4. 입력으로 주어진 모든 이동 후, 킹과 돌의 마지막 위치 구하기.
  4-1. 인덱스가 아닌, 체스판 형식의 "행과 열" 방식으로 좌표 구하기.
       - Ex) (7, 0) -> (1, A) => "A1" 출력
'''

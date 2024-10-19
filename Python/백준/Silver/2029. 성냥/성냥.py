from sys import stdin
from pprint import pprint


def solution():
    broken_match = 0  # 사라진 성냥 개수
    all_square = 0

    # 1. 사라진 가로 성냥
    for r in range(0, 10, 3):
        for c in range(1, 9, 3):
            if lst[r][c] != '-':
                broken_match += 1

    # 2. 사라진 세로 성냥
    for r in range(1, 9, 3):
        for c in range(0, 10, 3):
            if lst[r][c] != '|':
                broken_match += 1

    # 3. 1 x 1 정사각형 찾기
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            if (lst[r][c + 1] == '-' and
                lst[r + 1][c] == '|' and
                lst[r + 1][c + 3] == '|' and
                lst[r + 3][c + 1] == '-'):
                all_square += 1
                # pass


    # 4. 2 x 2 정사각형 찾기
    for r in range(0, 6, 3):
        for c in range(0, 6, 3):
            if (lst[r][c + 1] == '-' and
                lst[r + 1][c] == '|' and
                lst[r + 1][c + 6] == '|' and
                lst[r + 4][c] == '|' and
                lst[r + 4][c + 6] == '|'and
                lst[r + 6][c + 1] == '-'):
                all_square += 1
                # pass

    # 5. 3 x 3 정사각형 찾기
    if (lst[0][1] == '-' and
        lst[0][8] == '-' and
        lst[1][0] == '|' and
        lst[1][9] == '|' and
        lst[8][0] == '|' and
        lst[8][9] == '|' and
        lst[9][1] == '-' and
        lst[9][8] == '-'):
        all_square += 1
        # pass

    return broken_match, all_square


lst = [list(stdin.readline().strip()) for _ in range(10)]

matches, square = solution()
print(matches, square)
# pprint(lst, width=60)

'''
  0123456789
0 +--+--+--+
1 |..|..|..|
2 |..|..|..|
3 +--+--+..+
4 |.....|..|
5 |.....|..|
6 +--+--+..+
7 |........|
8 |........|
9 +--+--+--+

# 핵심 : '+'는 항상 있음, 성냥 반쪽은 없음. 이를 기준으로 가로, 세로 탐색해서 정사각형 찾기
# 1 x 1 경우 각 4변의 1칸 씩만 존재하는지 보면 되는 식.

가로 : 0, 3, 6, 9 / 12, 45, 78
세로 : 12, 45, 78 / 0, 3, 6, 9

2 / 0 / 1 
'''
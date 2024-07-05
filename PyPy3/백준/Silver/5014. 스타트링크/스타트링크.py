from sys import stdin, stdout
from collections import deque
from pprint import pprint

# 1 <= S, G <= F <= 1,000,000 / 0 <= U, D <= 1,000,000
F, S, G, U, D = map(int, stdin.readline().split())
# 건물 높이, 현재 위치, 목표 층, 위로, 아래로.


# 82% - 틀렸습니다.
def bfs(start):
    qu = deque()
    visited = [False] * (F + 1)
    cnt = 0
    move = [U, -D]
    visited[start] = True

    qu.append([start, cnt])

    if S == G:
        return 0
    elif S > G and D == 0:
        return -1
    elif S < G and U == 0:
        return -1

    while qu:
        cur, cnt = qu.popleft()
        # print(qu)
        # print(f'Cur={cur}, Cnt={cnt}')

        for k in range(2):  # 0 1
            nxt = cur + move[k]

            if nxt > F or nxt < 1 or visited[nxt]:
                continue

            if nxt != G:
                if not visited[nxt]:
                    visited[nxt] = True
                    qu.append([nxt, cnt+1])

            if nxt == G:
                return cnt+1
    else:
        return -1


res = bfs(S)

if res == -1:
    print("use the stairs")
else:
    print(res)

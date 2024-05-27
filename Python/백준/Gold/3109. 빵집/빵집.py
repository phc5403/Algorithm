## BOJ 3109 - 빵집 ##
from sys import stdin
from pprint import pprint


def dfs(x, y, cnt):
    global res, visited
    # print(f'({x}, {y}) / {cnt}, {res}')
    # pprint(visited, width=60)
    # print()

    visited[x][y] = True

    for k in range(3):
        # 다음 방향으로 향하기 전, 현재 알고 있는 파이프라인 수와 갱신 된 전체 파이프라인 수와 같지 않을 때만 진행.
        # 같다면, 다음 방향으로 탐색하는 X개의 루트 중 성공한 것이 존재하므로 더이상 현재 위치에서 다음 위치를 탐색 할 필요 없음.
        if cnt + 1 != res:
            nx = x + dx[k]
            ny = y + dy[k]
        else:
            break

        if nx < 0 or nx >= R or ny < 0 or ny >= C or visited[nx][ny] or lst[nx][ny] == 'x':
            continue
        else:
            visited[nx][ny] = True
            # 파이프라인이 완성 된 경우
            if ny == C - 1:
                # pprint(visited, width=60)
                res += 1
                return
            dfs(nx, ny, cnt)

# 최종점 N에서 다음 탐색 시 정답을 찾고 return 하면,
# 최정점 N-1에서부터도 돌면 안됨. -> 이 경우의 가지치기 할 조건은??


R, C = map(int,stdin.readline().split())
lst = [list(stdin.readline().strip()) for _ in range(R)]
# pprint(lst, width=40)
visited = [[False] * C for _ in range(R)]
# pprint(v, width=60)

# 우상 우 우하
dx = [-1, 0, 1]
dy = [1, 1, 1]
res = 0  # 파이프라인의 최대 개수

for r in range(R):
    # print(f'-----루프 {r+1} 번째 -------- ')
    visited[r][0] = True
    dfs(r, 0, res)

print(res)
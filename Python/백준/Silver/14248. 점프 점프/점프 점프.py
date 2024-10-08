from sys import stdin


def dfs(cur):
    global res

    for nxt in (cur + lst[cur], cur - lst[cur]):
        if 0 <= nxt < N and not visited[nxt]:
            res += 1
            visited[nxt] = 1
            dfs(nxt)


N = int(stdin.readline())  # 돌 개수
lst = list(map(int, stdin.readline().split()))
S = int(stdin.readline())  # 출발점

res = 1  # 시작점 돌 밟은 상태
visited = [0] * N

# 현재 위치, 방문 체크, 방문 횟수
dfs(S - 1)
print(res)

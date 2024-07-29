import sys

# 1 <= N <= 10만
N = int(sys.stdin.readline())

# 1 <= age <= 200 / 1 <= len(name) <= 100
# 인덱스 번호 -> 가입한 순서
lst = [list(sys.stdin.readline().split()) for _ in range(N)]

lst.sort(key=lambda x: int(x[0]))

for y in lst:
    print(*y)

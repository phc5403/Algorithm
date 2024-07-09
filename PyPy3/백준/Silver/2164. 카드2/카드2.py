from sys import stdin
from collections import deque

# 콜렉션 deque 없이 하려했는데 시간초과로 안됨.
# 그냥 대놓고 deque 콜렉션 쓰라는 문제같음. (밑에 오답 제출한 로직은 맞음)

N = int(stdin.readline())
qu = deque()

for i in range(1, N+1):
    qu.append(i)

while len(qu) != 1:
    qu.popleft()
    qu.rotate(-1)
    # rotate() = 가장 오른쪽 데이터를 pop() -> appendleft()
    # 인자는 수행 횟수인데, -1을 주면 반대로 순회함.

print(qu[0])

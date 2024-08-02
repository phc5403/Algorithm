import sys
from sys import stdin
from collections import deque

# 0 = deque / 1 = stack
N = int(stdin.readline())
data_structure = list(map(int, stdin.readline().split()))  # 자료구조 종류
numbers = list(map(int, stdin.readline().split()))  # 자료구조에 들어있는 초기 원소
M = int(stdin.readline().strip())  # 삽입할 숫자 개수
insert_nums = list(map(int, stdin.readline().split()))  # 삽입할 숫자들

qu = deque()
for i in range(N):
    if not data_structure[i]:
        qu.appendleft(numbers[i])

else:
    if not qu:
        print(*insert_nums)
        sys.exit()

for idx in range(M):
    qu.append(insert_nums[idx])
    print(qu.popleft(), end=' ')

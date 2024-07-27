from sys import stdin

N = int(stdin.readline())
lst = list(map(int, stdin.readline().split()))
stack = []
res = [-1] * N

stack.append(0)
for i in range(1, len(lst)):
    while stack and lst[stack[-1]] < lst[i]:
        res[stack.pop()] = lst[i]

    stack.append(i)

print(*res)

from sys import stdin

N  = int(stdin.readline())
stack = []
for i in range(N):
    oper = list(map(int, stdin.readline().split()))
    
    if oper[0] == 1:
        stack.append(oper[1])
    elif oper[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif oper[0] == 3:
        print(len(stack))
    elif oper[0] == 4:
        if stack:
            print(0)
        else:
            print(1)
    elif oper[0] == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)
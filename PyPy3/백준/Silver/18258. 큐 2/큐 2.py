from sys import stdin

## 백준#18258 문제를 위한 구현.
## 시간 복잡도 O(n) -> O(1)로 바꾸기 위해 ind(인덱스 위치 변수) 활용.
## 시간은 빠른데, 내가 원했던 Class 기반의 구현 방식이 아닌 문제를 위한 구현임.

N = int(stdin.readline())
qu = []
ind = 0

for i in range(N):
    oper = stdin.readline().strip().split()

    if oper[0] == 'push':
        qu.append(int(oper[1]))

    elif oper[0] == 'pop':
        if len(qu) == ind:  # 비어 있으면
            print(-1)
        else:
            print(qu[ind])
            ind += 1

    elif oper[0] == 'size':
        print(len(qu) - ind)

    elif oper[0] == 'empty':
        if len(qu) == ind:  # 비어 있으면
            print(1)
            ind = 0
            qu = []
        else:
            print(0)

    elif oper[0] == 'front':
        if len(qu) == ind:  # 비어 있으면
            print(-1)
        else:
            print(qu[ind])

    elif oper[0] == 'back':
        if len(qu) == ind:  # 비어 있으면
            print(-1)
        else:
            print(qu[-1])


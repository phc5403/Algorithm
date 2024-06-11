from sys import stdin


def snack():
    stack = []
    num = 1  # 다음 순서로 와야 할 숫자

    for cur in lst:  # 대기열 앞에서부터 검사
        # 턴 마다, 대기열과 스택 둘 다 확인해봐야 함.

        # 1. 스택 확인
        while stack and stack[-1] == num:
            stack.pop()
            num += 1

        # 2. 대기열 확인
        if cur == num:
            num += 1
        else:  # 2-1. 스택에 없고, 대기열 순번도 안맞다면 스택에 삽입 
            stack.append(cur)

    # 마지막으로 남아있는 스택 확인
    while stack and stack[-1] == num:
        stack.pop()
        num += 1

    if num == N + 1:
        return True
    else:
        return False


# Main #
N = int(stdin.readline())
lst = map(int, stdin.readline().split())

print("Nice") if snack() else print("Sad")

T = int(input())  # 3

cnt = 0

while T:

    S = input()
    temp = []

    check = True

    for x, y in zip(S, S[1:]):
        if x == y:  # 연속되면.
            if x not in temp:
                temp.append(x)
        else:  # 연속되지 않으면.
            if y in temp:
                check = False
            if x not in temp:
                temp.append(x)

    if check:
        cnt += 1

    T -= 1
    # print(temp, check)

print(cnt)

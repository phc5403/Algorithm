from sys import stdin

res = []

while True:
    number = stdin.readline().strip()

    if number == "0":
        break

    cnt = 2  # 호수판 경계의 여백 2cm는 고정

    for n in number:
        if n == '0':
            cnt += 4
        elif n == '1':
            cnt += 2
        else:
            cnt += 3

    # 각 숫자 사이에는 1cm의 여백이 들어감
    cnt += len(number) - 1
    res.append(cnt)

print(*res, sep='\n')
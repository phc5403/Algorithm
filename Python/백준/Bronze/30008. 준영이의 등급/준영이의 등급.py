from sys import stdin

N, K = map(int, stdin.readline().split())
subject = list(map(int, stdin.readline().split()))

res = []

for idx in range(K):
    grade = int(subject[idx] * 100 / N)

    if 0 <= grade <= 4:
        res.append(1)
    elif 4 < grade <= 11:
        res.append(2)
    elif 11 < grade <= 23:
        res.append(3)
    elif 23 < grade <= 40:
        res.append(4)
    elif 40 < grade <= 60:
        res.append(5)
    elif 60 < grade <= 77:
        res.append(6)
    elif 77 < grade <= 89:
        res.append(7)
    elif 89< grade <= 96:
        res.append(8)
    elif 96 < grade <= 100:
        res.append(9)

print(*res)
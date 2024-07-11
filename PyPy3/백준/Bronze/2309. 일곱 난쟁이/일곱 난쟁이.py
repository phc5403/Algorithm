from sys import stdin, stdout


def comb(arr, n):
    temp = []

    if n > len(arr):
        return temp

    if n == 1:
        for i in arr:
            temp.append([i])

    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in comb(arr[i + 1:], n - 1):
                temp.append([arr[i]] + j)

    return temp


lst = sorted([int(stdin.readline()) for _ in range(9)])
# print(comb(lst, 7))
# print(len(comb(lst, 7)))  # 9C7 = 9! / (7!2!) = 72 / 2 = 36
res = comb(lst, 7)
for r in res:
    if sum(r) == 100:
        print(*r, sep='\n')
        break
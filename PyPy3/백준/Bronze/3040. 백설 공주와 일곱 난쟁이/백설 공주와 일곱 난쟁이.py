from sys import stdin, stdout


def brute_force():
    sum_lst = sum(lst)

    for i in range(9):
        for j in range(i+1, 9):
            if sum_lst - (lst[i] + lst[j]) == 100:
                lst[i], lst[j] = 0, 0
                return


lst = sorted([int(stdin.readline()) for _ in range(9)])
brute_force()
print(*[res for res in lst if res], sep='\n')
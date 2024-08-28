from sys import stdin

# 100 <= N <= 20억
N = stdin.readline().strip()
F = int(stdin.readline().strip())

N = N[:len(N) - 2]

# 정답이 되는 N의 마지막 두 자리(한자리이면 앞에 '0' 추가)
res = ''

# N은 최소 3자리
for i in range(10):
    for j in range(10):
        temp = N + str(i) + str(j)

        if int(temp) % F == 0 and not res:
            res = temp[len(temp)-2:]
            break

if len(res) < 2:
    res = '0' + res
else:
    print(res)
    
from sys import stdin

N = int(stdin.readline())
chat = set()
cnt = 0

for _ in range(N):
    msg = stdin.readline().strip()

    if msg == "ENTER":
        cnt += len(chat)
        chat = set()
    else:
        chat.add(msg)

cnt += len(chat)
print(cnt)


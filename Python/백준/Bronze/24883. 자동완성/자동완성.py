from sys import stdin

alphabet = stdin.readline().strip()

if alphabet == 'N' or alphabet == 'n':
    print("Naver D2")
else:
    print("Naver Whale")
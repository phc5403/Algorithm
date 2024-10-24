from sys import stdin

prize = int(stdin.readline())

print(int(prize * 0.78), int(prize * 0.956))

'''
1. N - (N * 0.22) = N(1 - (1 * 0.22)) = N(1 - 0.22) = 0.78N ==> N * 0.78
2. N - (N * 0.2 * 0.22) = N(1 - (1 * 0.2 * 0.22)) = N(1 - 0.044) = 0.956N = N * 0.956
'''
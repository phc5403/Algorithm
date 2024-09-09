from sys import stdin

N = int(stdin.readline())

if N % 2 == 0:
    print("Duck")
else:
    print("Goose")

'''
애드혹(Ad-Hoc) 알고리즘.
해당 문제를 풀기 위해, 잘 알려진 정교한 알고리즘을 적용하지 않가 해결할 수 있는 유형의 문제.
즉, 정형화된 방법론이 아니라, 그 문제를 풀기 위한 창의적인 아이디어.
'''

'''
게임 과정을 그려보면, 
짝수일 때 Duck 승리
홀수일 때 Goose가 승리하게 되어있음.

Ex) N = 4
Turn 1_D턴) D 0 0 G
Turn 2_G턴) 0 D 0 G 
Turn 3_G턴) 0 D G 0 
Turn 4_D턴) D 승리
'''

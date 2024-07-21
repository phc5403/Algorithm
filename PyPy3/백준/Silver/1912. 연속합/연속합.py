## 이전 오답 코드 = 이중 반복문 = O(n^2)
## 현재 코드 = 반복문 1개 = O(n) // 구글링
from sys import stdin

N = int(stdin.readline())

num = list(map(int, stdin.readline().split()))

res = [0] * N
res[0] = num[0]

for i in range(1, N):
    res[i] = max(num[i], num[i] + res[i-1])

print(max(res))

'''
1. 현재 위치(i)가 음수인 경우1 -> 이전 연속합에 더했을 때도 음수면,
   다음 위치가 양수든 음수든 무조건 lst[i+1]가 단독 최댓값이 된다.
   
2. 현재 위치(i)가 음수인 경우2 -> 이전 연속합에 더했을 때 양수면,
   다음 위치가 양수면 계속 더해나가면 되고(누적합),
   다음 위치가 음수면 max()로 또 비교하면서 진행하면 됨.
   
3. 즉, 직전까지의 연속합 res[i-1]가 양수 = 다음 원소 num[i] + res[i-1]이 최댓값.
   직전까지의 연속합 res[i-1] 음수 = 다음 원소 num[i]가 최댓값.
'''

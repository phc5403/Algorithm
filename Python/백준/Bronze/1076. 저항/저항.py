from sys import stdin

resistance = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9,
}

lst = [stdin.readline().strip() for _ in range(3)]
res = ""
multiplication = 1

# 처음 색 2개는 저항의 값 -> 숫자 붙이기
for i in range(2):
    res += str(resistance[lst[i]])

# 마지막 색의 곱해야 하는 값 -> 저항값의 곱을 10에 제곱한 값.
multiplication = pow(10, resistance[lst[2]])

print(int(res) * multiplication)
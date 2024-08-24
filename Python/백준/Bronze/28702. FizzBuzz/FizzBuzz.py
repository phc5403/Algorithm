from sys import stdin

lst = [stdin.readline().strip() for _ in range(3)]
res = 0

for idx in range(2, -1, -1):
    if lst[idx].isdigit():
        res = int(lst[idx]) + (3 - idx)

if res % 3 == 0 and res % 5 == 0:
    print("FizzBuzz")
elif res % 3 == 0 and res % 5 != 0:
    print("Fizz")
elif res % 3 != 0 and res % 5 == 0:
    print("Buzz")
else:  # 3의 배수도 아니고, 5의 배수도 아닌 경우.
    print(res)

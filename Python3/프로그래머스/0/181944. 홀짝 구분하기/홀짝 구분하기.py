from sys import stdin

n = int(stdin.readline().strip())
is_even = "even"

if n % 2 == 1:
    is_even = "odd"
    
print(f'{n} is {is_even}')
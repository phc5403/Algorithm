from sys import stdin

str = stdin.readline().strip()
res = ""

for s in str:
    if 97 <= ord(s) <= 122:
        res += chr(ord(s) - 32)
    elif 65 <= ord(s) <= 90:
        res += chr(ord(s) + 32)
        
print(res)


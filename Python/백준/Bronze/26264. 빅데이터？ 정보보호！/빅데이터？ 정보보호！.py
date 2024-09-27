from sys import stdin

N = int(stdin.readline())

string = stdin.readline().strip()
len_string = len(string)
idx= 0
security, bigdata = 0, 0

while idx < len_string:
    if string[idx] == 's' and idx < len_string:
        idx += 8
        security += 1

    elif string[idx] == 'b' and idx < len_string:
        idx += 7
        bigdata += 1

if security > bigdata:
    print("security!")
elif bigdata > security:
    print("bigdata?")
else:
    print("bigdata? security!")

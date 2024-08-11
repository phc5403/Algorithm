lst = list(input())

for i in range(len(lst)):
    if ord(lst[i]) >= 97 or ord(lst[i]) <= 122:
        lst[i] = lst[i].upper()

check = set(lst)
check = list(check)
count = []

for x in check:
    count.append(lst.count(x))

temp = []
mmax = max(count)
result = ""
for a in count:
    if a not in temp:
        temp.append(a)
        result = check[count.index(max(count))]
    else:
        if a == mmax:
            result = "?"


print(result)

from sys import stdin

dad_body, dad_tail = stdin.readline().split()
mom_body, mom_tail = stdin.readline().split()

res = set()

for body in {dad_body, dad_tail, mom_body, mom_tail}:
    for tail in {dad_body, dad_tail, mom_body, mom_tail}:
        res.add((body, tail))

sorted_res = sorted(res)

for body, tail in sorted_res:
    print(body, tail)
def solution(a, b, c):
    answer = 0
    
    if a != b and b != c and c != a:
        answer = a + b + c
    elif len(set([a, b, c])) == 2:
        answer = (a + b + c) * (pow(a, 2) + pow(b, 2) + pow(c, 2))
    elif a == c and b == c and c == a:
        answer = (a + b + c) * (pow(a, 2) + pow(b, 2) + pow(c, 2)) *(pow(a, 3) + pow(b, 3) + pow(c, 3)) 
    
    return answer
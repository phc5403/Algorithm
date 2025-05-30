def solution(s):
    lst = []
    
    for cur in s.split():
        if cur == 'Z':
            if lst:
                lst.pop()
        else:
            lst.append(int(cur))
            
    return sum(lst)
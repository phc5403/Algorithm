def solution(ineq, eq, n, m):
    answer = 0
    
    chk = [">=", "<=", ">", "<"]
    
    if eq == "!":
        eq = ""
    temp = ineq + eq
    oper = chk.index(temp)
    
    if oper == 0:
        if n >= m:
            answer = 1
    elif oper == 1:
        if n <= m:
            answer = 1
    elif oper == 2:
        if n > m:
            answer = 1
    elif oper == 3:
        if n < m:
            answer = 1
            
    return answer
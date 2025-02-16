def solution(myString):
    answer = ''
    
    # A 65 ~ 90
    # a 97 ~ 122
    
    for s in myString:
        if ord(s) == 97:
            answer += chr(65)
        elif 66 <= ord(s) <= 90:
            answer += chr(ord(s) + 32)
        else:
            answer += chr(ord(s))
    
    return answer
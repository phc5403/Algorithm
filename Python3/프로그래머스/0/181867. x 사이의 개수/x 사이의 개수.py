def solution(myString):
    answer = []
    temp = myString.split("x")

    for t in temp:
        answer.append(len(t))
    
    return answer
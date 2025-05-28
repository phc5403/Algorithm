def solution(s1, s2):
    answer = 0
    
    for ss1 in range(len(s1)):
        for ss2 in range(len(s2)):
            if s1[ss1] == s2[ss2]:
                answer += 1
                
    return answer
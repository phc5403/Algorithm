def solution(name, yearning, photo):
    answer = []
    score = {}  # 인물별 점수를 저장할 딕셔너리
    
    # 1. 인물별 점수를 딕셔너리에 저장
    for idx in range(len(name)):
        if name[idx] not in score:
            score[name[idx]] = yearning[idx]
            
    # 2. photo를 순회하면서 채점
    for pht in photo:
        hab = 0  # 각 사진별 추억 점수
        for i in pht:
            if i in score:
                hab += score[i]
        answer.append(hab)        
        
        
    
    
    return answer

'''
1. 인물별 점수를 딕셔너리에 저장
2-1. photo 순회하면서 딕셔너리에 점수 있으면 채점
2-2. 딕셔너리에 점수 없으면 넘어감

'''
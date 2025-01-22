def solution(k, score):
    answer = []  # 매일 발표된 명예의 전당의 최하위 점수
    
    hall_of_fame = [float('inf')] * k
    days = len(score)  # 총 경연 일수
    
    for i in range(days):
        
        # 초기에 k일까지는 모든 점수가 명예의 전당에 기입
        if i + 1 <= k:
            hall_of_fame[i] = score[i]
        else:  # k + 1일부터 점수 경쟁
            min_fame = min(hall_of_fame)  # 명예의 전당 최하 점수
            min_fame_idx = hall_of_fame.index(min_fame)  # 명예의 전당 최하 점수의 인덱스 
            
            # 현재 점수와 최하 점수를 교체
            if score[i] > min_fame:
                hall_of_fame[min_fame_idx] = score[i]
                
        
        '''
        명예의 전당 최하위 점수만 return 할 것이므로,
        매 일수 마다 명예의 전당의 점수를 정렬할 필요 없음.
        '''
        answer.append(min(hall_of_fame))
        
        # print(answer, hall_of_fame)

        
        
    print(answer)
    
    return answer

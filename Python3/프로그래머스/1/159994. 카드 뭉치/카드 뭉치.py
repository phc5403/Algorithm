from collections import deque

def solution(cards1, cards2, goal):
    answer = ''
    
    check_cards1 = 0
    check_cards2 = 0
    comb = deque(goal)
    
    flag = True
    
    while comb:
        cur = comb.popleft()
        # print(cur, check_cards1, check_cards2)
        
        if check_cards1 < len(cards1) and cur == cards1[check_cards1]:  # 카드1과 일치
            check_cards1 += 1
        elif check_cards2 < len(cards2) and cur == cards2[check_cards2]:  # 카드2와 일치
            check_cards2 += 1
        else:  # 모두 불일치
            flag = False
            break
            
        # print(cur, check_cards1, check_cards2)
        # print()
            
    if flag:
        answer = "Yes"
    else:
        answer = "No"
    
    
    return answer
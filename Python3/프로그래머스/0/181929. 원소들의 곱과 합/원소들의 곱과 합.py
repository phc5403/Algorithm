def solution(num_list):
    answer = 0
    
    all_mul, all_hab = 1, 0
    
    for n in num_list:
        all_mul *= n
        all_hab += n
        
    all_hab = pow(all_hab, 2)  # 모든 원소들의 합의 제곱
    
    if all_mul < all_hab:
        answer = 1
    else:
        answer = 0
    
    return answer
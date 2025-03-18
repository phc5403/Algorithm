def solution(a, b):
    ans1 = 2 * a * b
    ans2 = int(str(a) + str(b))  # a ⊕ b
    
    if ans1 == ans2:
        return ans2
    
    return max(ans1, ans2)
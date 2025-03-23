def solution(num_list):
    odd_sum = sum(num_list[::2])   # 0, 2, 4, ... (홀수 번째 원소들)
    even_sum = sum(num_list[1::2]) # 1, 3, 5, ... (짝수 번째 원소들)
    return max(odd_sum, even_sum)

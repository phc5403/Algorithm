def solution(my_string, indices):
    indices_set = set(indices)  # 빠른 조회를 위해 set 변환
    return ''.join([char for i, char in enumerate(my_string) if i not in indices_set])

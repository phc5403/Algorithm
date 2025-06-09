def solution(s):
    return ''.join(sorted([ch for ch in set(s) if s.count(ch) == 1]))

def solution(code):
    mode = 0  # 초기 mode는 0
    ret = []  # 문자열을 저장할 리스트

    for idx, char in enumerate(code):
        if char == "1":
            mode = 1 - mode  # mode 전환
        else:
            if (mode == 0 and idx % 2 == 0) or (mode == 1 and idx % 2 == 1):
                ret.append(char)  # 조건 만족 시 추가

    return ''.join(ret) if ret else "EMPTY"

import re

def solution(myStr):
    parts = re.split("[abc]", myStr)  # 'a', 'b', 'c' 기준으로 나누기
    result = [p for p in parts if p]  # 빈 문자열 제거
    return result if result else ["EMPTY"]

def solution(arr, queries):
    for i, j in queries:
        arr[i], arr[j] = arr[j], arr[i]  # 스왑
    return arr
